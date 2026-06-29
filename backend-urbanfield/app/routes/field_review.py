from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import app, db
from app.models import Field, User, FieldReview

@app.route('/field_reviews', methods=['POST', 'GET'])
def manage_field_reviews():
    if request.method == 'GET':
        field_reviews = FieldReview.query.all()
        field_reviews_list = [{"id": fr.id, "field_id": fr.field_id, "user_id": fr.user_id, "rating": fr.rating, "review": fr.review} for fr in field_reviews]
        return jsonify(field_reviews_list), 200

    @jwt_required()
    def handle_post():
        data = request.json
        if not data or not data.get('field_id') or data.get('rating') is None or not data.get('review'):
            return jsonify({"error": "Missing required review fields"}), 400

        field_id = data.get('field_id')
        rating = data.get('rating')
        review = data.get('review')

        # Limit rating to 1-5
        try:
            rating = int(rating)
            if not (1 <= rating <= 10):
                return jsonify({"error": "Rating must be between 1 and 10"}), 400
        except ValueError:
            return jsonify({"error": "Rating must be an integer"}), 400

        # Enforce user identity from JWT
        current_identity = get_jwt_identity()
        current_user_id = current_identity.get('id') if isinstance(current_identity, dict) else current_identity

        field = db.session.get(Field, field_id)
        if not field:
            return jsonify({"error": f"Field with ID {field_id} not found"}), 404

        user = db.session.get(User, current_user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        new_field_review = FieldReview(field_id=field_id, user_id=current_user_id, rating=rating, review=review)
        db.session.add(new_field_review)
        db.session.commit()
        return jsonify({"message": "Field review created successfully"}), 201

    return handle_post()