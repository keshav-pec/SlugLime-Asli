import os
import secrets

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex(32))
    # Use instance folder for database - construct absolute path
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", f"sqlite:///{os.path.join(basedir, 'instance', 'app.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB uploads
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", os.path.join(basedir, "uploads"))
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:5173,http://localhost:3000")  # lock this down in production
    
    # Server configuration
    FLASK_HOST = os.getenv("FLASK_HOST", "127.0.0.1")
    FLASK_PORT = int(os.getenv("FLASK_PORT", "5000"))
