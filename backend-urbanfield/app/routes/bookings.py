from flask import request, jsonify
from app import app, db
from app.models import Booking, User, Field, PaymentMethod
import datetime

@app.route('/bookings', methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_bookings():
    if request.method == 'POST':
        data = request.json
        booking_time = datetime.datetime.strptime(data['time'], '%H:%M').time()

        # Cegah double-booking: tolak jika field+date+time yang sama sudah ada booking lain
        existing_booking = Booking.query.filter_by(
            field_id=data['field_id'],
            date=data['date'],
            time=booking_time
        ).first()
        if existing_booking:
            return jsonify({"error": "Slot waktu ini sudah dibooking, silakan pilih jadwal lain"}), 409

        new_booking = Booking(
            user_id=data['user_id'],
            field_id=data['field_id'],
            date=data['date'],
            time=booking_time,
            payment_method_id=data['payment_method_id']
        )
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Booking created successfully"}), 201
    
    elif request.method == 'GET':
        user_id = request.args.get('user_id')
        if user_id:
            bookings = Booking.query.filter_by(user_id=user_id).all()
        else:
            bookings = Booking.query.all()
        bookings_list = []
        for booking in bookings:
            user = User.query.get(booking.user_id)
            field = Field.query.get(booking.field_id)
            payment = PaymentMethod.query.get(booking.payment_method_id)
            booking_data = {
                "id": booking.id,
                "user_id": booking.user_id,
                "user_name": user.username,
                "field_id": booking.field_id,
                "field_name": field.name,
                "date": booking.date,
                "time": booking.time.strftime('%H:%M'),
                "payment_method_id": booking.payment_method_id,
                "payment_method_name": payment.method
            }
            bookings_list.append(booking_data)
        return jsonify(bookings_list), 200

    elif request.method == 'PUT':
        data = request.json
        booking_id = data.get('id')
        booking = Booking.query.get(booking_id)
        if booking:
            booking.user_id = data.get('user_id', booking.user_id)
            booking.field_id = data.get('field_id', booking.field_id)
            booking.date = data.get('date', booking.date)
            booking.time = datetime.datetime.strptime(data['time'], '%H:%M').time()  # Parse time string to datetime.time
            booking.payment_method_id = data.get('payment_method_id', booking.payment_method_id)
            db.session.commit()
            return jsonify({"message": "Booking updated successfully"}), 200
        else:
            return jsonify({"error": "Booking not found"}), 404

    elif request.method == 'DELETE':
        data = request.json
        booking_id = data.get('id')
        booking = Booking.query.get(booking_id)
        if booking:
            if booking.date < datetime.date.today():
                return jsonify({"error": "Booking yang sudah lewat tidak bisa dibatalkan"}), 400
            db.session.delete(booking)
            db.session.commit()
            return jsonify({"message": "Booking deleted successfully"}), 200
        else:
            return jsonify({"error": "Booking not found"}), 404

@app.route('/fields/<int:field_id>/booked_slots', methods=['GET'])
def get_booked_slots(field_id):
    date = request.args.get('date')
    if not date:
        return jsonify({"error": "Query parameter 'date' is required"}), 400

    bookings = Booking.query.filter_by(field_id=field_id, date=date).all()
    booked_times = [booking.time.strftime('%H:%M') for booking in bookings]
    return jsonify(booked_times), 200