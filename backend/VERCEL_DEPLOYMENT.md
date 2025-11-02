# Vercel Deployment Fix - SlugLime Backend

## ✅ Changes Made to Fix 500 Error

### 1. Created `vercel_app.py`
- Proper Vercel entry point that imports the Flask app
- No initialization code that could crash on import

### 2. Updated `vercel.json`
- Changed entry point from `app.py` to `vercel_app.py`
- Removed unnecessary `FLASK_ENV` variable

### 3. Fixed `app.py`
- Moved database initialization inside `create_app()` with proper error handling
- Database tables now created within app context (safe for serverless)
- Added try/catch to prevent crashes if database is unavailable

### 4. Updated `config.py`
- Added production domains to default CORS origins
- Fixed CORS to use configured origins instead of wildcard

### 5. Created `.vercelignore`
- Excludes unnecessary files from deployment
- Reduces deployment size and build time

## 🚀 How to Deploy

### Step 1: Set Environment Variables in Vercel Dashboard

Go to: https://vercel.com/dashboard → Your Project → Settings → Environment Variables

**Required Variables:**
```
SECRET_KEY=<generate-using-python-secrets-token-hex-32>
DATABASE_URL=<your-postgresql-connection-string>
CORS_ORIGINS=https://sluglime.vercel.app,https://sluglime.in,https://www.sluglime.in
```

**To generate SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Step 2: Set Up Database

**Option 1: Vercel Postgres (Recommended)**
1. Go to Vercel Dashboard → Storage → Create Database
2. Select Postgres
3. Copy the connection string
4. It will automatically set `DATABASE_URL` environment variable

**Option 2: External PostgreSQL**
Use any PostgreSQL provider:
- Supabase: https://supabase.com/
- Railway: https://railway.app/
- Neon: https://neon.tech/
- ElephantSQL: https://elephantsql.com/

Format: `postgresql://user:password@host:port/database?sslmode=require`

### Step 3: Deploy

```bash
cd backend
vercel --prod
```

Or push to GitHub if you have auto-deployment enabled.

### Step 4: Verify Deployment

Test the health endpoint:
```bash
curl https://sluglime-b.vercel.app/api/v1/health
```

Should return:
```json
{
  "status": "healthy",
  "message": "SlugLime backend is running",
  "version": "1.0.0"
}
```

Test public reports:
```bash
curl https://sluglime-b.vercel.app/api/v1/reports/public
```

## 🔍 Troubleshooting

### Still Getting 500 Error?

1. **Check Vercel Logs:**
   ```bash
   vercel logs sluglime-b
   ```
   Or visit: https://vercel.com/dashboard → Your Project → Deployments → Latest → Logs

2. **Verify Environment Variables:**
   - Ensure `SECRET_KEY` is set
   - Ensure `DATABASE_URL` is set and correct
   - Check CORS_ORIGINS includes your frontend domains

3. **Database Connection:**
   - Verify database is accessible from Vercel
   - Check connection string format
   - Ensure SSL is enabled for PostgreSQL

4. **Check Requirements:**
   - All dependencies in `requirements.txt`
   - Python version 3.10+ specified

### Common Issues

**Issue: Database connection fails**
- Solution: Ensure `DATABASE_URL` is set in Vercel dashboard
- Solution: Use `postgresql://` not `postgres://` (auto-fixed in config)
- Solution: Add `?sslmode=require` to connection string

**Issue: CORS errors**
- Solution: Verify `CORS_ORIGINS` includes your frontend URL
- Solution: Check both http/https variants

**Issue: Import errors**
- Solution: Ensure all dependencies are in `requirements.txt`
- Solution: Check Python version compatibility

## 📝 File Structure for Vercel

```
backend/
├── vercel_app.py        ← Vercel entry point (NEW)
├── app.py               ← Flask app factory
├── config.py            ← Configuration
├── database.py          ← Database setup
├── models.py            ← SQLAlchemy models
├── schemas.py           ← Validation schemas
├── security.py          ← Auth utilities
├── requirements.txt     ← Python dependencies
├── vercel.json          ← Vercel config (UPDATED)
└── .vercelignore        ← Exclude files (NEW)
```

## ✨ What's Different from Local Development

### Local Development:
- Uses SQLite database in `instance/` folder
- Files uploaded to `uploads/` folder
- Run with `python app.py`

### Vercel Production:
- Uses PostgreSQL database (persistent)
- File uploads need cloud storage (Vercel filesystem is read-only)
- Runs automatically via `vercel_app.py`
- Environment variables set in Vercel dashboard

## 🎯 Next Steps

1. ✅ Deploy backend to Vercel
2. ✅ Set up PostgreSQL database
3. ✅ Configure environment variables
4. ✅ Test all API endpoints
5. 🔲 Update frontend to use production API URL
6. 🔲 Set up cloud storage for file uploads (if needed)

## 📞 Support

If issues persist:
1. Check Vercel function logs
2. Verify all environment variables
3. Test database connection separately
4. Review Vercel Python runtime docs: https://vercel.com/docs/functions/runtimes/python
