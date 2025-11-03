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
try:
    from app import app, init_db  # type: ignore
    print("✓ Flask app imported successfully")
    
    # Initialize database tables on first cold start (idempotent - safe to call multiple times)
    try:
        init_db()
        print("✓ Database initialized")
    except Exception as e:
        print(f"⚠ Database initialization skipped: {e}")
        # Continue anyway - app can still serve requests without DB init
        
except Exception as e:
    print(f"✗ CRITICAL: Failed to import Flask app: {e}")
    import traceback
    traceback.print_exc()
    raise

# Vercel expects a handler or an app variable
# The app variable is the WSGI application
handler = app
