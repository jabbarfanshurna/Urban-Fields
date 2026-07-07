from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import app, db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

# Helper decorator to require admin role
def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            # Verify JWT will be handled by jwt_required where applicable,
            # but we can check the identity for role here.
            current_user_id = get_jwt_identity()
            if not current_user_id:
                return jsonify({"error": "Unauthorized"}), 401
            
            # Extract role from identity dictionary
            role = current_user_id.get('role') if isinstance(current_user_id, dict) else None
            if role != 'admin':
                return jsonify({"error": "Admin privilege required"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper

# Create a new user (Registration)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or not data.get('username') or not data.get('password') or not data.get('email') or not data.get('phone_number'):
        return jsonify({"error": "Missing required fields"}), 400

    # Prevent registration as admin directly unless authorized (or disable it for public route)
    role = data.get('role', 'customer')
    if role == 'admin':
        # Check if an admin is creating this admin
        # For simplicity, if we want to allow initial admin setup, we can check if there are any admins.
        # Otherwise, restrict admin creation to existing authenticated admins.
        admin_count = User.query.filter_by(role='admin').count()
        if admin_count > 0:
            return jsonify({"error": "Cannot register as admin directly. Only an existing admin can create another admin."}), 403

    # Check if username or email already exists
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "Username already exists"}), 400
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already exists"}), 400

    hashed_password = generate_password_hash(data['password'])
    new_user = User(
        username=data['username'],
        password=hashed_password,
        email=data['email'],
        phone_number=data['phone_number'],
        role=role
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

# Get all users (Admin gets all, Customer gets only admins)
@app.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    current_identity = get_jwt_identity()
    current_role = current_identity.get('role') if isinstance(current_identity, dict) else None

    if current_role == 'admin':
        users = User.query.all()
    else:
        users = User.query.filter_by(role='admin').all()

    users_list = [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "phone_number": user.phone_number,
            "role": user.role
        }
        for user in users
    ]
    return jsonify(users_list), 200

# Update a user (Self or Admin)
@app.route('/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.json
    current_identity = get_jwt_identity()
    current_user_id = current_identity.get('id') if isinstance(current_identity, dict) else current_identity
    current_role = current_identity.get('role') if isinstance(current_identity, dict) else 'customer'

    if current_user_id != user_id and current_role != 'admin':
        return jsonify({"error": "Unauthorized to update this user"}), 403

    user = db.session.get(User, user_id)
    if user:
        user.username = data.get('username', user.username)
        if 'password' in data and data['password']:
            user.password = generate_password_hash(data['password'])
        user.email = data.get('email', user.email)
        user.phone_number = data.get('phone_number', user.phone_number)
        
        # Only admin can change role
        if 'role' in data:
            if current_role == 'admin':
                user.role = data['role']
            else:
                return jsonify({"error": "Only admins can change roles"}), 403
                
        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

# Get specific user (Self or Admin)
@app.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    current_identity = get_jwt_identity()
    current_user_id = current_identity.get('id') if isinstance(current_identity, dict) else current_identity
    current_role = current_identity.get('role') if isinstance(current_identity, dict) else 'customer'

    if current_user_id != user_id and current_role != 'admin':
        return jsonify({"error": "Unauthorized to view this user"}), 403

    user = db.session.get(User, user_id)
    if user:
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "phone_number": user.phone_number,
            "role": user.role
        }), 200
    else:
        return jsonify({"message": "User not found"}), 404

# Delete a user (Self or Admin)
@app.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    current_identity = get_jwt_identity()
    current_user_id = current_identity.get('id') if isinstance(current_identity, dict) else current_identity
    current_role = current_identity.get('role') if isinstance(current_identity, dict) else 'customer'

    if current_user_id != user_id and current_role != 'admin':
        return jsonify({"error": "Unauthorized to delete this user"}), 403

    user = db.session.get(User, user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "User not found"}), 404

# Login route (Verify hashed password)
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"message": "Email and password are required"}), 400
        
    email = data['email']
    password = data['password']
    user = User.query.filter_by(email=email).first()
    
    if user and check_password_hash(user.password, password):
        # Storing id and role in identity dict so we don't have to query DB repeatedly
        access_token = create_access_token(identity={"id": user.id, "role": user.role})
        return jsonify({"message": "Login successful", "access_token": access_token}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
    
# User profile route
@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_identity = get_jwt_identity()
    current_user_id = current_identity.get('id') if isinstance(current_identity, dict) else current_identity
    user = db.session.get(User, current_user_id)
    
    if user:
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "phone_number": user.phone_number,
            "role": user.role
        }), 200
    else:
        return jsonify({"message": "User not found"}), 404

# Endpoint to handle user document uploads
@app.route('/users/<int:user_id>/documents', methods=['POST'])
@jwt_required()
def upload_user_document(user_id):
    current_identity = get_jwt_identity()
    current_user_id = current_identity.get('id') if isinstance(current_identity, dict) else current_identity
    
    if current_user_id:
        if current_user_id == user_id:
            return jsonify({"message": "Document uploaded successfully"}), 200
        else:
            return jsonify({"error": "Unauthorized"}), 403
    else:
        return jsonify({"error": "Authorization token missing"}), 401