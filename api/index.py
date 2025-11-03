"""
Vercel serverless function entry point.
This file must be in the api/ directory for Vercel's Python runtime.

CRITICAL: Vercel's Python runtime expects the WSGI app to be named 'app' (not 'handler')
"""
import sys
import os

# Add the backend directory to the Python path
backend_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'backend')
sys.path.insert(0, backend_dir)

# Import the Flask app
# Note: Pylance may show an import error, but this works at runtime
# because we added backend/ to sys.path above
try:
    from app import app as flask_app, init_db  # type: ignore
    print("✓ Flask app imported successfully")
    
    # DON'T initialize database on import - let it happen on first request
    # This prevents cold start failures if DB is temporarily unavailable
    # Tables will be created automatically when first accessed
    
except Exception as e:
    print(f"✗ CRITICAL: Failed to import Flask app: {e}")
    import traceback
    traceback.print_exc()
    # Re-raise to prevent Vercel from serving a broken app
    raise

# CRITICAL: Vercel expects the WSGI application to be named 'app'
# This is the actual Flask application that will handle requests
app = flask_app
