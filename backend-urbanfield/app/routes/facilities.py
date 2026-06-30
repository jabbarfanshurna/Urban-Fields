from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import app, db
from app.models import Facility
from app.routes.users import admin_required

@app.route('/facilities', methods=['GET'])
def get_facilities():
    facilities = Facility.query.all()
    facilities_list = [{"id": facility.id, "name": facility.name, "icon": facility.icon} for facility in facilities]
    return jsonify(facilities_list), 200

@app.route('/facilities', methods=['POST', 'PUT', 'DELETE'])
@jwt_required()
@admin_required()
def write_facilities():
    if request.method == 'POST':
        data = request.json
        if not data or not data.get('name') or not data.get('icon'):
            return jsonify({"error": "Missing required fields"}), 400
        new_facility = Facility(name=data['name'], icon=data['icon'])
        db.session.add(new_facility)
        db.session.commit()
        return jsonify({"message": "Facility created successfully"}), 201
    
    elif request.method == 'PUT':
        data = request.json
        facility_id = data.get('id')
        if not facility_id:
            return jsonify({"error": "Facility ID is required"}), 400
        facility = db.session.get(Facility, facility_id)
        if facility:
            facility.name = data.get('name', facility.name)
            facility.icon = data.get('icon', facility.icon)
            db.session.commit()
            return jsonify({"message": "Facility updated successfully"}), 200
        else:
            return jsonify({"error": "Facility not found"}), 404

    elif request.method == 'DELETE':
        data = request.json
        facility_id = data.get('id')
        if not facility_id:
            return jsonify({"error": "Facility ID is required"}), 400
        facility = db.session.get(Facility, facility_id)
        if facility:
            db.session.delete(facility)
            db.session.commit()
            return jsonify({"message": "Facility deleted successfully"}), 200
        else:
            return jsonify({"error": "Facility not found"}), 404

