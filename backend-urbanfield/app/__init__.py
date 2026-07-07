from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger
import os

app = Flask(__name__)

# Buka pintu CORS untuk frontend
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:5173"]}}, supports_credentials=True)

# Konfigurasi Database dan JWT
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/urban_fields'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'ewakofields_rahasia_123' # Kunci JWT dipindah ke sini
app.config['JWT_VERIFY_SUB'] = False

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Swagger UI - dokumentasi API bisa diakses di /apidocs
app.config['SWAGGER'] = {
    'title': 'Urban Fields API',
    'uiversion': 3,
    'specs_route': '/apidocs/',
}
swagger_yml_path = os.path.join(os.path.dirname(__file__), 'swagger.yml')
swagger = Swagger(app, template_file=swagger_yml_path)

# Import routes (pastikan di bawah inisialisasi app, db, jwt)
from app.routes import users, bookings, facilities, field_facility, field_review, field_types, fields, payments