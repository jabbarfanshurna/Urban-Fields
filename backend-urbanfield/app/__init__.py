from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)

# Buka pintu CORS untuk frontend
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:5173"]}}, supports_credentials=True)

# Konfigurasi Database dan JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/urban_fields'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'ewakofields_rahasia_123' # Kunci JWT dipindah ke sini

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Import routes (pastikan di bawah inisialisasi app, db, jwt)
from app.routes import bookings, facilities, field_facility, field_review, field_types, fields, payments, users