# SlugLime

A secure, anonymous whistleblowing and social platform built with Flask and React. SlugLime enables users to submit anonymous reports, track their status, and engage with a social feed—all while maintaining privacy and security.

## 🌟 Features

### Whistleblowing System
- **Anonymous Reporting**: Submit reports without revealing your identity
- **Secure Access**: Unique ticket IDs and access codes for report tracking
- **Status Tracking**: Monitor your report's progress (open, in progress, resolved, closed)
- **Two-way Communication**: Exchange messages with moderators securely
- **File Attachments**: Upload supporting documents (PDF, DOCX, images, videos up to 25MB)

### Social Feed
- **User Authentication**: Secure registration and login with Argon2 password hashing
- **Post Creation**: Share content with images and captions
- **Engagement**: Like, comment, and save posts
- **Public Reports**: View whistleblower reports in the main feed

### Security Features
- **Argon2 Password Hashing**: Industry-standard password protection
- **JWT Token Authentication**: Secure session management with timed expiration
- **CORS Protection**: Configurable cross-origin resource sharing
- **Access Code Verification**: Hash-based report access control
- **Anonymous Submissions**: No IP or identity tracking for whistleblowers

## 🏗️ Project Structure

```
SlugLime-Asli/
├── backend/                 # Flask REST API
│   ├── app.py              # Main application & routes
│   ├── config.py           # Configuration settings
│   ├── database.py         # Database initialization
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Marshmallow validation schemas
│   ├── security.py         # Authentication & hashing utilities
│   ├── requirements.txt    # Python dependencies
│   ├── .env.example        # Environment variables template
│   └── README.md           # Backend documentation
│
└── frontend/               # React SPA
    ├── src/
    │   ├── components/     # Reusable UI components
    │   │   ├── Navbar.jsx
    │   │   ├── Footer.jsx
    │   │   └── BrandLogo.jsx
    │   ├── pages/          # Page components
    │   │   ├── Home.jsx         # Main feed
    │   │   ├── Submit.jsx       # Anonymous submission form
    │   │   ├── Status.jsx       # Report tracking
    │   │   ├── About.jsx
    │   │   └── Contact.jsx
    │   ├── api.js          # API client functions
    │   ├── App.jsx         # Main app component
    │   └── theme.css       # Global styles
    ├── package.json
    └── README.md           # Frontend documentation
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+** (Python 3.12 recommended)
- **Node.js 18+** and npm
- **Git**

### Backend Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/keshav-pec/SlugLime-Asli.git
   cd SlugLime-Asli/backend
   ```

2. **Create and activate virtual environment**:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   ```bash
   # Windows
   copy .env.example .env

   # macOS/Linux
   cp .env.example .env
   ```
   
   Edit `.env` and set a secure `SECRET_KEY`:
   ```env
   SECRET_KEY=your-secure-random-key-here-use-secrets.token_hex(32)
   ```

5. **Run the Flask server**:
   ```bash
   python app.py
   ```
   
   Backend will be available at `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd ../frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start development server**:
   ```bash
   npm run dev
   ```
   
   Frontend will be available at `http://localhost:5173`

4. **Open in browser**:
   Visit `http://localhost:5173`

## 🔧 Configuration

### Backend Environment Variables

Create a `.env` file in the `backend/` directory:

```env
# Flask Configuration
SECRET_KEY=your-secure-random-key-here

# Database
DATABASE_URI=sqlite:///instance/app.db

# CORS (comma-separated origins)
CORS_ORIGINS=http://localhost:5173,http://localhost:3000

# Uploads
UPLOAD_FOLDER=uploads
```

### Frontend API Configuration

The API endpoint is configured in `frontend/src/api.js`:
```javascript
const API = "http://localhost:5000";
```

For production, move this to an environment variable.

## 📡 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login user

### Reports (Whistleblowing)
- `GET /api/v1/reports/public` - Get public reports feed
- `POST /api/v1/reports` - Create anonymous report
- `GET /api/v1/reports/<ticket>?code=<access_code>` - Get specific report
- `POST /api/v1/reports/<ticket>/messages?code=<access_code>` - Post message

### Social Feed
- `GET /api/v1/feed` - Get feed posts
- `POST /api/v1/posts` - Create post (authenticated)
- `POST /api/v1/posts/<id>/like` - Like/unlike post
- `POST /api/v1/posts/<id>/save` - Save/unsave post
- `POST /api/v1/posts/<id>/comments` - Add comment

See `backend/README.md` for detailed API documentation.

## 🛠️ Tech Stack

### Backend
- **Flask 3.0.3** - Web framework
- **Flask-SQLAlchemy 3.1.1** - ORM
- **Flask-CORS 4.0.0** - CORS handling
- **Marshmallow 3.21.3** - Object serialization & validation
- **Argon2-cffi 23.1.0** - Password hashing
- **itsdangerous 2.2.0** - Token signing & verification
- **Passlib 1.7.4** - Password utilities
- **Python-dotenv 1.0.1** - Environment management

### Frontend
- **React 18** - UI library
- **Vite** - Build tool & dev server
- **React Router DOM** - Client-side routing
- **Lucide React** - Icon library
- **Custom CSS** - Styling with CSS variables

## 🧪 Testing

### Backend Tests
```bash
cd backend
python -m pytest
```

### Manual API Testing
See `backend/__TESTS__/smoke_test` for curl examples.

## 📦 Production Deployment

### Backend

1. Set environment variables properly
2. Use a production WSGI server (Gunicorn):
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```
3. Use PostgreSQL or MySQL instead of SQLite
4. Configure proper CORS origins
5. Enable HTTPS

### Frontend

1. Build for production:
   ```bash
   npm run build
   ```
2. Serve the `dist/` folder with Nginx or Apache
3. Update API endpoint to production URL
4. Enable HTTPS

## 🔒 Security Considerations

- Never commit `.env` files
- Always set a strong `SECRET_KEY` in production
- Use HTTPS in production
- Implement rate limiting for API endpoints
- Regularly update dependencies
- Review uploaded files for malware
- Set up proper backup strategies for the database

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Keshav** - [keshav-pec](https://github.com/keshav-pec)

## 🙏 Acknowledgments

- Built with ❤️ for secure, anonymous communication
- Inspired by the need for safe whistleblowing platforms

---

**Note**: This is a demonstration project. For production use, implement additional security measures, proper error handling, logging, monitoring, and compliance with local data protection regulations.
