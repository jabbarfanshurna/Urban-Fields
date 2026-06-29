from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import app, db
from app.models import PaymentMethod, Payment, Booking
from app.routes.users import admin_required
import datetime

@app.route('/payments', methods=['POST', 'GET', 'PUT', 'DELETE'])
@jwt_required()
def manage_payments():
    current_identity = get_jwt_identity()
    current_user_id = current_identity.get('id') if isinstance(current_identity, dict) else current_identity
    current_role = current_identity.get('role') if isinstance(current_identity, dict) else 'customer'

    if request.method == 'POST':
        data = request.json
        if not data or not data.get('booking_id') or not data.get('amount') or not data.get('payment_date'):
            return jsonify({"error": "Missing required payment fields"}), 400

        booking = db.session.get(Booking, data['booking_id'])
        if not booking:
            return jsonify({"error": "Booking not found"}), 404

        # Restriction: Customer can only pay for their own booking
        if booking.user_id != current_user_id and current_role != 'admin':
            return jsonify({"error": "Unauthorized to create payment for this booking"}), 403

        try:
            pay_date = datetime.datetime.strptime(data['payment_date'], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            # Fallback to today if format doesn't match
            pay_date = datetime.datetime.now()

        new_payment = Payment(
            booking_id=data['booking_id'],
            amount=data['amount'],
            payment_date=pay_date
        )
        db.session.add(new_payment)
        db.session.commit()
        return jsonify({"message": "Payment created successfully"}), 201
    
    elif request.method == 'GET':
        # Restriction: Customer can only view their own payments, Admin can view all
        if current_role == 'admin':
            payments = Payment.query.all()
        else:
            payments = Payment.query.join(Booking).filter(Booking.user_id == current_user_id).all()

        payments_list = [
            {
                "id": payment.id,
                "booking_id": payment.booking_id,
                "amount": float(payment.amount),
                "payment_date": payment.payment_date.strftime('%Y-%m-%d %H:%M:%S') if payment.payment_date else None
            }
            for payment in payments
        ]
        return jsonify(payments_list), 200

    elif request.method == 'PUT':
        # Only admin should edit payment details directly
        if current_role != 'admin':
            return jsonify({"error": "Unauthorized. Admin privileges required to update payments."}), 403

        data = request.json
        payment_id = data.get('id')
        if not payment_id:
            return jsonify({"error": "Payment ID is required"}), 400

        payment = db.session.get(Payment, payment_id)
        if payment:
            payment.booking_id = data.get('booking_id', payment.booking_id)
            payment.amount = data.get('amount', payment.amount)
            if 'payment_date' in data:
                try:
                    payment.payment_date = datetime.datetime.strptime(data['payment_date'], '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    return jsonify({"error": "Invalid date format. Expected YYYY-MM-DD HH:MM:S"}), 400
            db.session.commit()
            return jsonify({"message": "Payment updated successfully"}), 200
        else:
            return jsonify({"error": "Payment not found"}), 404

    elif request.method == 'DELETE':
        # Only admin should delete payments
        if current_role != 'admin':
            return jsonify({"error": "Unauthorized. Admin privileges required to delete payments."}), 403

        data = request.json
        payment_id = data.get('id')
        if not payment_id:
            return jsonify({"error": "Payment ID is required"}), 400

        payment = db.session.get(Payment, payment_id)
        if payment:
            db.session.delete(payment)
            db.session.commit()
            return jsonify({"message": "Payment deleted successfully"}), 200
        else:
            return jsonify({"error": "Payment not found"}), 404