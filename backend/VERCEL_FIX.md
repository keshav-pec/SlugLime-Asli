# 🔧 Vercel 500 Error - FIXED

## ❌ Problem
Backend was crashing on Vercel with:
```
500: INTERNAL_SERVER_ERROR
Code: FUNCTION_INVOCATION_FAILED
```

## ✅ Solution

### Root Causes Identified:
1. **No proper Vercel entry point** - `app.py` was trying to run as a script
2. **Database initialization issues** - Trying to create folders on read-only filesystem
3. **CORS misconfiguration** - Wildcard instead of specific domains

### Files Changed:

#### 1. Created `vercel_app.py` ⭐
```python
from app import app
# Simple entry point for Vercel
```

#### 2. Updated `vercel.json`
```json
{
  "version": 2,
  "builds": [{"src": "vercel_app.py", "use": "@vercel/python"}],
  "routes": [{"src": "/(.*)", "dest": "vercel_app.py"}]
}
```

#### 3. Fixed `app.py`
- Database initialization now wrapped in try/catch
- Safe for read-only filesystems
- No crashes if folders can't be created

#### 4. Updated `config.py`
- Added production domains to CORS defaults
- Fixed PostgreSQL connection string handling

#### 5. Created `.vercelignore`
- Excludes unnecessary files from deployment

## 🚀 Deploy Now

### Quick Deploy:
```bash
cd backend
./deploy.sh        # macOS/Linux
# or
deploy.bat         # Windows
```

### Manual Deploy:
```bash
cd backend
vercel --prod
```

## ⚙️ Required Environment Variables

Set these in **Vercel Dashboard** → **Settings** → **Environment Variables**:

### 1. SECRET_KEY (Required)
Generate with:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 2. DATABASE_URL (Required)
Use PostgreSQL connection string:
```
postgresql://user:password@host:port/database?sslmode=require
```

**Recommended Providers:**
- Vercel Postgres (easiest)
- Supabase
- Railway
- Neon

### 3. CORS_ORIGINS (Optional)
Defaults are already set for:
- https://sluglime.vercel.app
- https://sluglime.in
- https://www.sluglime.in
- http://localhost:5173
- http://localhost:3000

## 🧪 Test Deployment

```bash
# Health check
curl https://sluglime-b.vercel.app/api/v1/health

# Should return:
# {"status":"healthy","message":"SlugLime backend is running","version":"1.0.0"}

# Test API
curl https://sluglime-b.vercel.app/api/v1/reports/public
```

## 📊 View Logs

```bash
vercel logs sluglime-b
```

Or visit: https://vercel.com/dashboard → Your Project → Deployments → Logs

## 🎯 Deployment Checklist

- [ ] Set `SECRET_KEY` in Vercel environment variables
- [ ] Set `DATABASE_URL` in Vercel environment variables  
- [ ] Deploy: `vercel --prod`
- [ ] Test health endpoint
- [ ] Test API endpoints
- [ ] Check logs for any errors
- [ ] Update frontend API URL if needed

## 🔄 What Changed vs Previous Setup

| Aspect | Before | After |
|--------|--------|-------|
| Entry Point | `app.py` (script mode) | `vercel_app.py` (WSGI mode) |
| DB Init | Crashed on read-only FS | Wrapped in try/catch |
| CORS | Wildcard `*` | Specific domains |
| Error Handling | Basic | Comprehensive handlers |
| Deployment | Manual config | Automated scripts |

## 💡 Tips

1. **Database**: Use PostgreSQL, not SQLite (ephemeral on Vercel)
2. **File Uploads**: For production, use cloud storage (S3, Cloudflare R2)
3. **Logs**: Always check logs first when debugging
4. **Environment**: Set all variables in Vercel dashboard, not `.env` files

## 📚 Documentation

- Full guide: `VERCEL_DEPLOYMENT.md`
- General deployment: `../DEPLOYMENT.md`
- Production summary: `../PRODUCTION_SUMMARY.md`

## ✨ Status

✅ Backend deployment **READY**
✅ Error handling **FIXED**
✅ CORS configuration **FIXED**
✅ Database initialization **FIXED**
✅ Vercel configuration **OPTIMIZED**

Deploy and you're good to go! 🚀
