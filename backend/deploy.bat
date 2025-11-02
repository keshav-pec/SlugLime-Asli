@echo off
REM SlugLime Backend - Vercel Deployment Script for Windows

echo ================================
echo SlugLime Backend Deployment
echo ================================
echo.

REM Check if vercel CLI is installed
where vercel >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Vercel CLI not found!
    echo Installing Vercel CLI...
    npm install -g vercel
    echo.
)

REM Check if we're in the backend directory
if not exist "vercel_app.py" (
    echo Error: Must run from backend directory
    echo Run: cd backend ^&^& deploy.bat
    exit /b 1
)

echo Vercel CLI found
echo.

REM Remind about environment variables
echo IMPORTANT: Ensure these environment variables are set in Vercel Dashboard:
echo    - SECRET_KEY (generate with: python -c "import secrets; print(secrets.token_hex(32))")
echo    - DATABASE_URL (PostgreSQL connection string)
echo    - CORS_ORIGINS (optional, defaults are set)
echo.

set /p REPLY="Have you set the environment variables? (y/n): "
if /i not "%REPLY%"=="y" (
    echo.
    echo Please set environment variables first:
    echo    1. Go to: https://vercel.com/dashboard
    echo    2. Select your project
    echo    3. Settings - Environment Variables
    echo.
    exit /b 1
)

echo.
echo Deploying to Vercel...
echo.

REM Deploy to production
vercel --prod

echo.
echo Deployment complete!
echo.
echo Test your deployment:
echo    Health check: curl https://sluglime-b.vercel.app/api/v1/health
echo    Reports API: curl https://sluglime-b.vercel.app/api/v1/reports/public
echo.
echo View logs: vercel logs sluglime-b
echo.
