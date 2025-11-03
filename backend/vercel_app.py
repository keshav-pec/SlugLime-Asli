"""
Vercel serverless function handler for SlugLime backend.
This file acts as the entry point when deploying from the backend/ directory.

To use this:
  cd backend
  vercel --prod

Alternatively, deploy from project root using api/index.py
"""
from app import app, init_db

# Initialize database tables on cold start
try:
    init_db()
except Exception as e:
    print(f"Warning: Database init skipped: {e}")

# Vercel expects the Flask app to be accessible as 'app'
# No need to call app.run() - Vercel handles that
