from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app import app, db
from app.models import FieldType
from app.routes.users import admin_required

@app.route('/field_types', methods=['POST', 'GET', 'PUT', 'DELETE'])
def manage_field_types():
    if request.method == 'GET':
        field_types = FieldType.query.all()
        field_types_list = [{"id": field_type.id, "name": field_type.name} for field_type in field_types]
        return jsonify(field_types_list), 200

    @jwt_required()
    @admin_required()
    def handle_write_operations():
        if request.method == 'POST':
            data = request.json
            if not data or not data.get('name'):
                return jsonify({"error": "Missing required field 'name'"}), 400
            new_field_type = FieldType(name=data['name'])
            db.session.add(new_field_type)
            db.session.commit()
            return jsonify({"message": "Field type created successfully"}), 201
        
        elif request.method == 'PUT':
            data = request.json
            field_type_id = data.get('id')
            if not field_type_id:
                return jsonify({"error": "Field type ID is required"}), 400
            field_type = db.session.get(FieldType, field_type_id)
            if field_type:
                field_type.name = data.get('name', field_type.name)
                db.session.commit()
                return jsonify({"message": "Field type updated successfully"}), 200
            else:
                return jsonify({"error": "Field type not found"}), 404

        elif request.method == 'DELETE':
            data = request.json
            field_type_id = data.get('id')
            if not field_type_id:
                return jsonify({"error": "Field type ID is required"}), 400
            field_type = db.session.get(FieldType, field_type_id)
            if field_type:
                db.session.delete(field_type)
                db.session.commit()
                return jsonify({"message": "Field type deleted successfully"}), 200
            else:
                return jsonify({"error": "Field type not found"}), 404

    return handle_write_operations()

