# Production Environment Summary

## URLs
- Frontend: https://sluglime.vercel.app, https://sluglime.in
- Backend: https://sluglime-b.vercel.app

## Environment Variables

### Backend (Vercel Dashboard)
```
SECRET_KEY=<generate-with-secrets.token_hex(32)>
DATABASE_URI=postgresql://user:pass@host:port/db
CORS_ORIGINS=https://sluglime.vercel.app,https://sluglime.in,https://www.sluglime.in
UPLOAD_FOLDER=/tmp/uploads
```

### Frontend (Vercel Dashboard)
```
VITE_API_URL=https://sluglime-b.vercel.app
```

## Quick Deploy Commands

```bash
# Backend
cd backend
vercel --prod

# Frontend
cd frontend
vercel --prod
```

## Key Files Modified

✅ `backend/config.py` - Added production CORS origins
✅ `backend/app.py` - Cleaned up code, removed unnecessary comments
✅ `backend/.env.example` - Simplified template
✅ `backend/.env.production` - Production config template
✅ `backend/vercel.json` - Vercel backend configuration
✅ `frontend/src/api.js` - Uses environment variable for API URL
✅ `frontend/.env` - Local development config
✅ `frontend/.env.example` - Template
✅ `frontend/.env.production` - Production API endpoint
✅ `frontend/vercel.json` - Frontend routing & caching config
✅ `DEPLOYMENT.md` - Complete deployment guide

## Security Notes
- CORS locked to production domains
- Environment variables managed via Vercel
- Passwords hashed with Argon2
- JWT tokens for authentication
- Access codes for anonymous reports

## Database Recommendation
Use PostgreSQL instead of SQLite for production:
- Vercel Postgres
- Supabase
- Railway
- Neon
