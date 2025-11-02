import os
import secrets

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", secrets.token_hex(32))
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", f"sqlite:///{os.path.join(basedir, 'instance', 'app.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", os.path.join(basedir, "uploads"))
    
    default_origins = "http://localhost:5173,http://localhost:3000,https://sluglime.vercel.app,https://sluglime.in,https://www.sluglime.in"
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", default_origins)
