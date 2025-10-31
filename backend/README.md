# Backend - Flask REST API# Backend - Flask API



The backend API for SlugLime, providing secure whistleblowing and social feed functionality.This is the backend API for the Slugime application, built with Flask.



## 🚀 Quick Start## Setup



### Installation1. Create and activate a virtual environment:

   ```bash

1. **Create and activate virtual environment**:   python -m venv venv

   ```bash   # Windows

   python -m venv venv   venv\Scripts\activate

      # macOS/Linux

   # Windows   source venv/bin/activate

   venv\Scripts\activate   ```

   

   # macOS/Linux2. Install dependencies:

   source venv/bin/activate   ```bash

   ```   pip install -r requirements.txt

   ```

2. **Install dependencies**:

   ```bash3. Configure environment variables:

   pip install -r requirements.txt   - Copy `.env.example` to `.env`

   ```   - Update `SECRET_KEY` with a secure random key

   - Adjust other settings as needed

3. **Configure environment**:

   ```bash4. Run the application:

   # Windows   ```bash

   copy .env.example .env   python app.py

      ```

   # macOS/Linux

   cp .env.example .envThe API will be available at `http://127.0.0.1:5000`

   ```

   ## Environment Variables

   Edit `.env` and set a secure `SECRET_KEY`:

   ```bash- `SECRET_KEY`: Secret key for session encryption (required in production)

   # Generate a secure key with Python:- `DATABASE_URI`: Database connection string (default: SQLite)

   python -c "import secrets; print(secrets.token_hex(32))"- `CORS_ORIGINS`: Comma-separated list of allowed origins

   ```- `UPLOAD_FOLDER`: Directory for file uploads



4. **Run the server**:## API Endpoints

   ```bash

   python app.py### Authentication

   ```- `POST /api/v1/auth/register` - Register a new user

   - `POST /api/v1/auth/login` - Login user

   The API will be available at `http://127.0.0.1:5000`

### Feed & Posts

## 🔧 Configuration- `GET /api/v1/feed` - Get feed posts

- `POST /api/v1/posts` - Create a new post

### Environment Variables- `POST /api/v1/posts/<id>/like` - Like/unlike a post

- `POST /api/v1/posts/<id>/save` - Save/unsave a post

Create a `.env` file with the following:- `POST /api/v1/posts/<id>/comments` - Add comment to post



```env### Whistleblower Reports

# Flask Configuration (REQUIRED in production)- `GET /api/v1/reports/public` - Get public reports

SECRET_KEY=your-secure-random-key-here- `POST /api/v1/reports` - Create anonymous report

- `GET /api/v1/reports/<ticket>` - Get specific report (requires access code)

# Database Configuration- `POST /api/v1/reports/<ticket>/messages` - Add message to report

DATABASE_URI=sqlite:///instance/app.db

## Security

# CORS Configuration (comma-separated origins)

CORS_ORIGINS=http://localhost:5173,http://localhost:3000- Passwords are hashed using Argon2

- Access codes for reports are hashed

# Upload Configuration- JWT tokens are used for authentication

UPLOAD_FOLDER=uploads- CORS is configured to restrict origins

```

## 📡 API Endpoints

### Authentication

#### Register User
```http
POST /api/v1/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "name": "John Doe",
  "password": "securepassword123"
}
```

#### Login
```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

### Whistleblower Reports

#### Create Anonymous Report
```http
POST /api/v1/reports
Content-Type: multipart/form-data

title: Report Title
body: Detailed description
category: corruption (optional)
file_0: [binary file data] (optional)
```

**Important**: Save the ticket and access code. They won't be shown again!

#### Get Public Reports
```http
GET /api/v1/reports/public
```

#### Get Specific Report (Requires Access Code)
```http
GET /api/v1/reports/{ticket}?code={access_code}
```

#### Post Message to Report
```http
POST /api/v1/reports/{ticket}/messages?code={access_code}
Content-Type: application/json

{
  "body": "Additional information..."
}
```

### Social Feed

#### Get Feed
```http
GET /api/v1/feed
Authorization: Bearer {token} (optional)
```

#### Create Post (Authenticated)
```http
POST /api/v1/posts
Authorization: Bearer {token}
Content-Type: application/json

{
  "image_url": "https://example.com/image.jpg",
  "caption": "Post caption"
}
```

#### Like/Unlike Post
```http
POST /api/v1/posts/{post_id}/like
Authorization: Bearer {token}
```

#### Save/Unsave Post
```http
POST /api/v1/posts/{post_id}/save
Authorization: Bearer {token}
```

#### Add Comment
```http
POST /api/v1/posts/{post_id}/comments
Authorization: Bearer {token}
Content-Type: application/json

{
  "body": "Comment text"
}
```

## 🔒 Security Features

### Password Security
- **Argon2** hashing with automatic salt generation
- Memory-hard algorithm resistant to GPU attacks

### Access Code Security
- Random 20-character codes (letters + digits)
- Argon2 hashing for storage
- Constant-time verification to prevent timing attacks

### Token Authentication
- **itsdangerous** URLSafeTimedSerializer for JWT-like tokens
- 30-day expiration (configurable)
- Signed with SECRET_KEY

### CORS Protection
- Configurable allowed origins
- Explicit method and header allowlists

### File Upload Security
- Secure filename sanitization
- File size limits (16MB max)
- Isolated storage directory

## 🧪 Testing

See `__TESTS__/smoke_test` for curl examples.

## 📦 Dependencies

- **Flask 3.0.3** - Web framework
- **Flask-SQLAlchemy 3.1.1** - ORM
- **Flask-CORS 4.0.0** - CORS handling
- **Marshmallow 3.21.3** - Validation
- **Argon2-cffi 23.1.0** - Password hashing
- **itsdangerous 2.2.0** - Token signing

## 🚀 Production Deployment

### Using Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Production Checklist

- [ ] Set strong `SECRET_KEY` environment variable
- [ ] Use PostgreSQL/MySQL instead of SQLite
- [ ] Enable HTTPS (reverse proxy with Nginx)
- [ ] Configure proper CORS origins (no wildcards)
- [ ] Set up logging and monitoring
- [ ] Implement rate limiting
- [ ] Regular database backups

## 📄 License

MIT License - See root LICENSE file for details.
