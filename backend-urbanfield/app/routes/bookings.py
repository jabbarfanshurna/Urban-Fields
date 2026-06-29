from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import app, db
from app.models import Booking, User, Field, PaymentMethod
import datetime

@app.route('/bookings', methods=['POST', 'GET', 'PUT', 'DELETE'])
@jwt_required()
def manage_bookings():
    current_identity = get_jwt_identity()
    current_user_id = current_identity.get('id') if isinstance(current_identity, dict) else current_identity
    current_role = current_identity.get('role') if isinstance(current_identity, dict) else 'customer'

    if request.method == 'POST':
        data = request.json
        if not data or not data.get('field_id') or not data.get('date') or not data.get('time') or not data.get('payment_method_id'):
            return jsonify({"error": "Missing required booking fields"}), 400

        # Secure user_id: normal customer cannot book for other users
        req_user_id = data.get('user_id', current_user_id)
        if req_user_id != current_user_id and current_role != 'admin':
            return jsonify({"error": "Unauthorized to create booking for another user"}), 403

        try:
            booking_time = datetime.datetime.strptime(data['time'], '%H:%M').time()
            booking_date = datetime.datetime.strptime(data['date'], '%Y-%m-%d').date()
        except ValueError:
            return jsonify({"error": "Invalid date or time format. Expected YYYY-MM-DD and HH:MM"}), 400

        # Cegah double-booking: tolak jika field+date+time yang sama sudah ada booking lain
        existing_booking = Booking.query.filter_by(
            field_id=data['field_id'],
            date=booking_date,
            time=booking_time
        ).first()
        if existing_booking:
            return jsonify({"error": "Slot waktu ini sudah dibooking, silakan pilih jadwal lain"}), 409

        new_booking = Booking(
            user_id=req_user_id,
            field_id=data['field_id'],
            date=booking_date,
            time=booking_time,
            payment_method_id=data['payment_method_id']
        )
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Booking created successfully"}), 201
    
    elif request.method == 'GET':
        user_id = request.args.get('user_id')
        # Restriction: Customer can only view their own bookings, admin can view all
        if current_role != 'admin':
            user_id = current_user_id

        if user_id:
            bookings = Booking.query.filter_by(user_id=user_id).all()
        else:
            bookings = Booking.query.all()

        bookings_list = []
        for booking in bookings:
            user = db.session.get(User, booking.user_id)
            field = db.session.get(Field, booking.field_id)
            payment = db.session.get(PaymentMethod, booking.payment_method_id)
            if not user or not field or not payment:
                continue
            booking_data = {
                "id": booking.id,
                "user_id": booking.user_id,
                "user_name": user.username,
                "field_id": booking.field_id,
                "field_name": field.name,
                "date": booking.date.strftime('%Y-%m-%d') if isinstance(booking.date, (datetime.date, datetime.datetime)) else str(booking.date),
                "time": booking.time.strftime('%H:%M'),
                "payment_method_id": booking.payment_method_id,
                "payment_method_name": payment.method
            }
            bookings_list.append(booking_data)
        return jsonify(bookings_list), 200

    elif request.method == 'PUT':
        data = request.json
        booking_id = data.get('id')
        if not booking_id:
            return jsonify({"error": "Booking ID is required"}), 400

        booking = db.session.get(Booking, booking_id)
        if not booking:
            return jsonify({"error": "Booking not found"}), 404

        # Restriction: Customer can only update their own booking
        if booking.user_id != current_user_id and current_role != 'admin':
            return jsonify({"error": "Unauthorized to update this booking"}), 403

        # Admin can update user_id
        if 'user_id' in data and current_role == 'admin':
            booking.user_id = data['user_id']
            
        booking.field_id = data.get('field_id', booking.field_id)
        if 'date' in data:
            try:
                booking.date = datetime.datetime.strptime(data['date'], '%Y-%m-%d').date()
            except ValueError:
                return jsonify({"error": "Invalid date format. Expected YYYY-MM-DD"}), 400
        if 'time' in data:
            try:
                booking.time = datetime.datetime.strptime(data['time'], '%H:%M').time()
            except ValueError:
                return jsonify({"error": "Invalid time format. Expected HH:MM"}), 400
        booking.payment_method_id = data.get('payment_method_id', booking.payment_method_id)
        
        db.session.commit()
        return jsonify({"message": "Booking updated successfully"}), 200

    elif request.method == 'DELETE':
        data = request.json
        booking_id = data.get('id')
        if not booking_id:
            return jsonify({"error": "Booking ID is required"}), 400

        booking = db.session.get(Booking, booking_id)
        if not booking:
            return jsonify({"error": "Booking not found"}), 404

        # Restriction: Customer can only cancel their own booking
        if booking.user_id != current_user_id and current_role != 'admin':
            return jsonify({"error": "Unauthorized to cancel this booking"}), 403

        # Allow cancellation only if booking date is today or in the future
        if booking.date < datetime.date.today():
            return jsonify({"error": "Booking yang sudah lewat tidak bisa dibatalkan"}), 400
        db.session.delete(booking)
        db.session.commit()
        return jsonify({"message": "Booking deleted successfully"}), 200

@app.route('/fields/<int:field_id>/booked_slots', methods=['GET'])
def get_booked_slots(field_id):
    date = request.args.get('date')
    if not date:
        return jsonify({"error": "Query parameter 'date' is required"}), 400

    try:
        query_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"error": "Invalid date format. Expected YYYY-MM-DD"}), 400

    bookings = Booking.query.filter_by(field_id=field_id, date=query_date).all()
    booked_times = [booking.time.strftime('%H:%M') for booking in bookings]
    return jsonify(booked_times), 200