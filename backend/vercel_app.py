"""
Vercel serverless function handler for SlugLime backend.
This file acts as the entry point for Vercel deployments.
"""
from app import app

# Vercel expects the Flask app to be accessible as 'app'
# No need to call app.run() - Vercel handles that
