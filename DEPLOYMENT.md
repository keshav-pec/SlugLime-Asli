# SlugLime Production Deployment Guide

## 🌐 Production URLs

- **Frontend**: 
  - Primary: https://sluglime.vercel.app
  - Custom Domain: https://sluglime.in
- **Backend**: https://sluglime-b.vercel.app

## 📋 Pre-Deployment Checklist

### Backend Setup

1. **Generate Secure Secret Key**
   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

2. **Set Vercel Environment Variables**
   - Go to Vercel Dashboard → sluglime-b project → Settings → Environment Variables
   - Add the following:
     ```
     SECRET_KEY=<your-generated-key>
     DATABASE_URI=<your-production-database-url>
     CORS_ORIGINS=https://sluglime.vercel.app,https://sluglime.in,https://www.sluglime.in
     UPLOAD_FOLDER=/tmp/uploads
     ```

3. **Database Setup**
   - SQLite won't persist on Vercel (ephemeral filesystem)
   - Use PostgreSQL (recommended):
     - [Vercel Postgres](https://vercel.com/docs/storage/vercel-postgres)
     - [Supabase](https://supabase.com/)
     - [Railway](https://railway.app/)
     - [Neon](https://neon.tech/)

### Frontend Setup

1. **Vercel Environment Variables**
   - Go to Vercel Dashboard → sluglime project → Settings → Environment Variables
   - Add for Production:
     ```
     VITE_API_URL=https://sluglime-b.vercel.app
     ```

2. **Custom Domain Configuration**
   - In Vercel Dashboard → sluglime project → Settings → Domains
   - Add domain: `sluglime.in`
   - Follow DNS configuration instructions

## 🚀 Deployment Steps

### Backend Deployment (Vercel)

1. **Install Vercel CLI** (if not already installed)
   ```bash
   npm i -g vercel
   ```

2. **Deploy Backend**
   ```bash
   cd backend
   vercel --prod
   ```

3. **Verify Backend**
   - Visit: https://sluglime-b.vercel.app/api/v1/reports/public
   - Should return empty reports array or existing reports

### Frontend Deployment (Vercel)

1. **Deploy Frontend**
   ```bash
   cd frontend
   vercel --prod
   ```

2. **Verify Frontend**
   - Visit: https://sluglime.vercel.app
   - Check all pages load correctly
   - Test API connectivity

## 🔒 Security Configuration

### CORS Settings

Backend automatically allows:
- https://sluglime.vercel.app
- https://sluglime.in
- https://www.sluglime.in
- http://localhost:5173 (for development)
- http://localhost:3000 (for development)

### Database Security

For PostgreSQL connection string format:
```
postgresql://username:password@host:port/database?sslmode=require
```

Always use SSL for production databases.

## 📁 File Structure

```
SlugLime-Asli/
├── backend/
│   ├── .env.example          # Template for environment variables
│   ├── .env.production       # Production environment template
│   ├── vercel.json           # Vercel backend configuration
│   └── ...
└── frontend/
    ├── .env                  # Local development config
    ├── .env.example          # Template for environment variables
    ├── .env.production       # Production environment config
    ├── vercel.json           # Vercel frontend configuration
    └── ...
```

## 🧪 Testing Production

### Test Backend Endpoints

```bash
# Test public reports
curl https://sluglime-b.vercel.app/api/v1/reports/public

# Test CORS (should return report data)
curl -H "Origin: https://sluglime.in" \
     https://sluglime-b.vercel.app/api/v1/reports/public
```

### Test Frontend

1. Visit https://sluglime.in
2. Test anonymous report submission
3. Test report status tracking
4. Verify all API calls work

## 🔧 Environment Files Summary

### Backend `.env.production`
```env
SECRET_KEY=<your-secure-key>
DATABASE_URI=<postgresql-connection-string>
CORS_ORIGINS=https://sluglime.vercel.app,https://sluglime.in,https://www.sluglime.in
UPLOAD_FOLDER=/tmp/uploads
```

### Frontend `.env.production`
```env
VITE_API_URL=https://sluglime-b.vercel.app
```

### Frontend `.env` (local development)
```env
VITE_API_URL=http://localhost:5000
```

## 📊 Monitoring

### Check Deployment Status
- Backend: https://vercel.com/dashboard → sluglime-b
- Frontend: https://vercel.com/dashboard → sluglime

### View Logs
```bash
# Backend logs
vercel logs sluglime-b

# Frontend logs
vercel logs sluglime
```

## 🐛 Troubleshooting

### CORS Errors
- Verify backend CORS_ORIGINS includes your frontend URL
- Check browser console for exact error
- Verify both HTTP/HTTPS protocols match

### Database Connection Errors
- Confirm DATABASE_URI is set correctly
- Check database service is running
- Verify SSL settings for PostgreSQL

### API 404 Errors
- Ensure backend is deployed and running
- Check VITE_API_URL in frontend environment
- Verify API routes in backend are correct

### File Upload Issues
- Vercel has 4.5MB body size limit
- Files stored in /tmp are ephemeral
- Consider using cloud storage (S3, Cloudflare R2) for production

## 🔄 Continuous Deployment

### GitHub Integration
1. Connect repository to Vercel
2. Enable automatic deployments
3. Set production branch to `main`
4. Configure environment variables in Vercel dashboard

### Deployment Triggers
- Push to `main` → Auto-deploy production
- Pull requests → Preview deployments

## 📝 Notes

- **SQLite Limitation**: Vercel's filesystem is ephemeral. Use PostgreSQL for production.
- **File Uploads**: Files in `/tmp` are temporary. Use cloud storage for persistent files.
- **Environment Variables**: Never commit `.env` files. Use Vercel dashboard.
- **Secret Key**: Generate a new secure key for production.
- **Custom Domain**: Configure DNS properly for `sluglime.in`.

## ✅ Post-Deployment Verification

- [ ] Backend health check passes
- [ ] Frontend loads on all domains
- [ ] CORS working correctly
- [ ] Database connected successfully
- [ ] Anonymous reports can be created
- [ ] Report status can be checked
- [ ] User authentication works
- [ ] Social feed displays correctly
- [ ] All API endpoints functional

## 🆘 Support

For issues, check:
- Vercel deployment logs
- Browser console errors
- Network tab for API calls
- Environment variables are set correctly
