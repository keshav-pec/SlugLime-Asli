"""
Vercel serverless function entry point.
This file must be in the api/ directory for Vercel's Python runtime.
"""
import sys
import os

# Add the backend directory to the Python path
backend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'backend')
sys.path.insert(0, backend_dir)

# Import the Flask app
# Note: Pylance may show an import error, but this works at runtime
# because we added backend/ to sys.path above
from app import app, init_db  # type: ignore

# Initialize database tables on first cold start (idempotent - safe to call multiple times)
try:
    init_db()
except Exception as e:
    print(f"Warning: Database initialization skipped: {e}")

# Vercel expects a handler or an app variable
# The app variable is the WSGI application
handler = app
