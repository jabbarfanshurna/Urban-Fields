from flask import Flask
from flask_cors import CORS
from config import Config
from models import db
from routes import bp

def create_app():
    app = Flask(__name__)
    
    # Memberikan izin resmi untuk localhost
    CORS(app, resources={r"/*": {"origins": ["http://localhost:5173"]}})
    
    app.config.from_object(Config) 
    app.config['JWT_SECRET_KEY'] = 'ewakofields_rahasia_123' # Bisa diisi teks apa saja
    db.init_app(app)
    app.register_blueprint(bp)

    return app