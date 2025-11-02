# Backend - Flask REST API# Backend - Flask REST API# Backend - Flask API



The backend API for SlugLime, providing secure whistleblowing and social feed functionality.



## 🚀 Quick StartThe backend API for SlugLime, providing secure whistleblowing and social feed functionality.This is the backend API for the Slugime application, built with Flask.



> **Note:** Python 3.10+ is required. Having issues? Run `python check_setup.py` to diagnose problems.



### Installation## 🚀 Quick Start## Setup



1. **Create and activate virtual environment**:

   ```bash

   python -m venv venv### Installation1. Create and activate a virtual environment:

   

   # Windows   ```bash

   venv\Scripts\activate

   1. **Create and activate virtual environment**:   python -m venv venv

   # macOS/Linux

   source venv/bin/activate   ```bash   # Windows

   ```

   python -m venv venv   venv\Scripts\activate

2. **Install dependencies**:

   ```bash      # macOS/Linux

   pip install -r requirements.txt

   ```   # Windows   source venv/bin/activate



3. **Configure environment**:   venv\Scripts\activate   ```

   ```bash

   # Windows   

   copy .env.example .env

      # macOS/Linux2. Install dependencies:

   # macOS/Linux

   cp .env.example .env   source venv/bin/activate   ```bash

   ```

      ```   pip install -r requirements.txt

   Edit `.env` and set a secure `SECRET_KEY`:

   ```bash   ```

   # Generate a secure key with Python:

   python -c "import secrets; print(secrets.token_hex(32))"2. **Install dependencies**:

   ```

   ```bash3. Configure environment variables:

4. **Verify setup (recommended)**:

   ```bash   pip install -r requirements.txt   - Copy `.env.example` to `.env`

   python check_setup.py

   ```   ```   - Update `SECRET_KEY` with a secure random key

   

   This script checks:   - Adjust other settings as needed

   - Python version (3.10+ required)

   - All dependencies installed correctly3. **Configure environment**:

   - `.env` file configuration

   - Database and directories can be created   ```bash4. Run the application:

   - Local modules can be imported

   # Windows   ```bash

5. **Run the server**:

   ```bash   copy .env.example .env   python app.py

   python app.py

   ```      ```

   

   The API will be available at `http://127.0.0.1:5000`   # macOS/Linux



## 🔧 Configuration   cp .env.example .envThe API will be available at `http://127.0.0.1:5000`



### Environment Variables   ```



Create a `.env` file with:   ## Environment Variables



```env   Edit `.env` and set a secure `SECRET_KEY`:

# Flask Configuration (REQUIRED in production)

SECRET_KEY=your-secure-random-key-here   ```bash- `SECRET_KEY`: Secret key for session encryption (required in production)



# Database Configuration   # Generate a secure key with Python:- `DATABASE_URI`: Database connection string (default: SQLite)

DATABASE_URI=sqlite:///instance/app.db

   python -c "import secrets; print(secrets.token_hex(32))"- `CORS_ORIGINS`: Comma-separated list of allowed origins

# CORS Configuration (comma-separated origins)

CORS_ORIGINS=http://localhost:5173,http://localhost:3000   ```- `UPLOAD_FOLDER`: Directory for file uploads



# Upload Configuration

UPLOAD_FOLDER=uploads

```4. **Run the server**:## API Endpoints



## 📡 API Endpoints   ```bash



### Authentication   python app.py### Authentication



#### Register User   ```- `POST /api/v1/auth/register` - Register a new user

```http

POST /api/v1/auth/register   - `POST /api/v1/auth/login` - Login user

Content-Type: application/json

   The API will be available at `http://127.0.0.1:5000`

{

  "email": "user@example.com",### Feed & Posts

  "name": "John Doe",

  "password": "securepassword123"## 🔧 Configuration- `GET /api/v1/feed` - Get feed posts

}

```- `POST /api/v1/posts` - Create a new post



#### Login### Environment Variables- `POST /api/v1/posts/<id>/like` - Like/unlike a post

```http

POST /api/v1/auth/login- `POST /api/v1/posts/<id>/save` - Save/unsave a post

Content-Type: application/json

Create a `.env` file with the following:- `POST /api/v1/posts/<id>/comments` - Add comment to post

{

  "email": "user@example.com",

  "password": "securepassword123"

}```env### Whistleblower Reports

```

# Flask Configuration (REQUIRED in production)- `GET /api/v1/reports/public` - Get public reports

### Whistleblower Reports

SECRET_KEY=your-secure-random-key-here- `POST /api/v1/reports` - Create anonymous report

#### Create Anonymous Report

```http- `GET /api/v1/reports/<ticket>` - Get specific report (requires access code)

POST /api/v1/reports

Content-Type: multipart/form-data# Database Configuration- `POST /api/v1/reports/<ticket>/messages` - Add message to report



title: Report TitleDATABASE_URI=sqlite:///instance/app.db

body: Detailed description

category: corruption (optional)## Security

file_0: [binary file data] (optional)

```# CORS Configuration (comma-separated origins)



**Important**: Save the ticket and access code. They won't be shown again!CORS_ORIGINS=http://localhost:5173,http://localhost:3000- Passwords are hashed using Argon2



#### Get Public Reports- Access codes for reports are hashed

```http

GET /api/v1/reports/public# Upload Configuration- JWT tokens are used for authentication

```

UPLOAD_FOLDER=uploads- CORS is configured to restrict origins

#### Get Specific Report (Requires Access Code)

```http```

GET /api/v1/reports/{ticket}?code={access_code}

```## 📡 API Endpoints



#### Post Message to Report### Authentication

```http

POST /api/v1/reports/{ticket}/messages?code={access_code}#### Register User

Content-Type: application/json```http

POST /api/v1/auth/register

{Content-Type: application/json

  "body": "Additional information..."

}{

```  "email": "user@example.com",

  "name": "John Doe",

### Social Feed  "password": "securepassword123"

}

#### Get Feed```

```http

GET /api/v1/feed#### Login

Authorization: Bearer {token} (optional)```http

```POST /api/v1/auth/login

Content-Type: application/json

#### Create Post (Authenticated)

```http{

POST /api/v1/posts  "email": "user@example.com",

Authorization: Bearer {token}  "password": "securepassword123"

Content-Type: application/json}

```

{

  "image_url": "https://example.com/image.jpg",### Whistleblower Reports

  "caption": "Post caption"

}#### Create Anonymous Report

``````http

POST /api/v1/reports

## 🔒 Security FeaturesContent-Type: multipart/form-data



- **Argon2** password hashingtitle: Report Title

- **JWT-like** token authentication (30-day expiration)body: Detailed description

- **Access code hashing** for report securitycategory: corruption (optional)

- **CORS protection** with configurable originsfile_0: [binary file data] (optional)

- **Secure file uploads** with sanitization```



## 🧪 Testing**Important**: Save the ticket and access code. They won't be shown again!



See `__TESTS__/smoke_test` for curl examples.#### Get Public Reports

```http

## ⚠️ TroubleshootingGET /api/v1/reports/public

```

### "Python 3.10 or higher is required"

Install Python 3.10+ from [python.org](https://www.python.org/downloads/)#### Get Specific Report (Requires Access Code)

```http

### "ModuleNotFoundError"GET /api/v1/reports/{ticket}?code={access_code}

```bash```

# Ensure venv is activated (should see (venv) in terminal)

pip install -r requirements.txt#### Post Message to Report

``````http

POST /api/v1/reports/{ticket}/messages?code={access_code}

### "SECRET_KEY not set" warningContent-Type: application/json

Create `.env` from `.env.example` and set SECRET_KEY

{

### Database errors  "body": "Additional information..."

```bash}

# Delete and recreate```

rm instance/app.db  # or: del instance\app.db on Windows

python app.py### Social Feed

```

#### Get Feed

### "Address already in use"```http

Port 5000 is busy. Change port in `app.py` or kill the process using it.GET /api/v1/feed

Authorization: Bearer {token} (optional)

## 🚀 Production Deployment```



### Using Gunicorn#### Create Post (Authenticated)

```http

```bashPOST /api/v1/posts

pip install gunicornAuthorization: Bearer {token}

gunicorn -w 4 -b 0.0.0.0:5000 app:appContent-Type: application/json

```

{

### Production Checklist  "image_url": "https://example.com/image.jpg",

  "caption": "Post caption"

- [ ] Set strong `SECRET_KEY` environment variable}

- [ ] Use PostgreSQL/MySQL instead of SQLite```

- [ ] Enable HTTPS (reverse proxy with Nginx)

- [ ] Configure proper CORS origins (no wildcards)#### Like/Unlike Post

- [ ] Set up logging and monitoring```http

- [ ] Implement rate limitingPOST /api/v1/posts/{post_id}/like

- [ ] Regular database backupsAuthorization: Bearer {token}

```

## 📦 Dependencies

#### Save/Unsave Post

- **Flask 3.0.3** - Web framework```http

- **Flask-SQLAlchemy 3.1.1** - ORMPOST /api/v1/posts/{post_id}/save

- **Flask-CORS 4.0.0** - CORS handlingAuthorization: Bearer {token}

- **Marshmallow 3.21.3** - Validation```

- **Argon2-cffi 23.1.0** - Password hashing

- **itsdangerous 2.2.0** - Token signing#### Add Comment

```http

## 📄 LicensePOST /api/v1/posts/{post_id}/comments

Authorization: Bearer {token}

MIT License - See root LICENSE file for details.Content-Type: application/json


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
