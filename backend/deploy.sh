#!/bin/bash

# SlugLime Backend - Vercel Deployment Script

echo "🚀 SlugLime Backend Deployment"
echo "================================"
echo ""

# Check if vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI not found!"
    echo "📦 Installing Vercel CLI..."
    npm install -g vercel
    echo ""
fi

# Check if we're in the backend directory
if [ ! -f "vercel_app.py" ]; then
    echo "❌ Error: Must run from backend directory"
    echo "💡 Run: cd backend && ./deploy.sh"
    exit 1
fi

echo "✅ Vercel CLI found"
echo ""

# Remind about environment variables
echo "⚠️  IMPORTANT: Ensure these environment variables are set in Vercel Dashboard:"
echo "   - SECRET_KEY (generate with: python -c 'import secrets; print(secrets.token_hex(32))')"
echo "   - DATABASE_URL (PostgreSQL connection string)"
echo "   - CORS_ORIGINS (optional, defaults are set)"
echo ""

read -p "Have you set the environment variables? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Please set environment variables first:"
    echo "   1. Go to: https://vercel.com/dashboard"
    echo "   2. Select your project"
    echo "   3. Settings → Environment Variables"
    echo ""
    exit 1
fi

echo ""
echo "🚀 Deploying to Vercel..."
echo ""

# Deploy to production
vercel --prod

echo ""
echo "✅ Deployment complete!"
echo ""
echo "🧪 Test your deployment:"
echo "   Health check: curl https://sluglime-b.vercel.app/api/v1/health"
echo "   Reports API: curl https://sluglime-b.vercel.app/api/v1/reports/public"
echo ""
echo "📊 View logs: vercel logs sluglime-b"
echo ""
