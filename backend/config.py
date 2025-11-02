import os
import secrets

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex(32))
    
    # Use instance folder for database - construct absolute path
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    # Database: Use DATABASE_URL (common on serverless platforms) or DATABASE_URI
    # Falls back to SQLite for local development
    database_url = os.getenv("DATABASE_URL") or os.getenv("DATABASE_URI")
    if not database_url:
        # Local development - use SQLite in instance folder
        database_url = f"sqlite:///{os.path.join(basedir, 'instance', 'app.db')}"
    
    # Vercel Postgres uses "postgres://" but SQLAlchemy 1.4+ requires "postgresql://"
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    
    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB uploads
    
    # Upload folder (note: serverless has read-only filesystem, use cloud storage in production)
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", os.path.join(basedir, "uploads"))
    
    # CORS: Allow all origins in dev, specific domains in production
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:5173,http://localhost:3000")
    
    # Server configuration (only used for local development)
    FLASK_HOST = os.getenv("FLASK_HOST", "127.0.0.1")
    FLASK_PORT = int(os.getenv("FLASK_PORT", "5000"))
