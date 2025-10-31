import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

# Local imports
from config import Config
from database import db
from models import Report, Message, User, Post, Comment, Like, Save
from schemas import (
    ReportCreateSchema, MessageCreateSchema, ReportPublicSchema,
    RegisterSchema, LoginSchema, UserPublicSchema, CommentPublicSchema
)
from security import (
    gen_ticket_id, gen_access_code, hash_code, verify_code,
    issue_token, verify_token
)

# Load environment variables
load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    # Setup CORS (Cross-Origin Resource Sharing)
    cors_origins = app.config.get("CORS_ORIGINS", "*")
    # Allow comma-separated origins in config (turn into list)
    if isinstance(cors_origins, str) and "," in cors_origins:
        cors_origins = [o.strip() for o in cors_origins.split(",") if o.strip()]
    CORS(app, resources={
        r"/api/*": {
            "origins": cors_origins,
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization", "X-Access-Code"],
            "expose_headers": ["Content-Type"],
            "supports_credentials": False
        }
    })

    # Initialize SQLAlchemy
    db.init_app(app)

    # Create necessary folders and tables
    with app.app_context():
        try:
            # Ensure instance folder exists for SQLite database (use Flask's instance_path)
            # This guarantees the folder is created at the expected absolute path
            os.makedirs(app.instance_path, exist_ok=True)
            # Ensure the configured upload folder exists (Config.UPLOAD_FOLDER is absolute)
            upload_folder = app.config.get("UPLOAD_FOLDER", os.path.join(app.instance_path, "uploads"))
            os.makedirs(upload_folder, exist_ok=True)
            # Create database tables
            db.create_all()
            print(f"✓ Database initialized at: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
            print(f"✓ Upload folder: {upload_folder}")
        except Exception as e:
            print(f"ERROR: Failed to initialize database or folders: {e}")
            raise

    # -----------------------
    # Helper Functions
    # -----------------------
    def get_current_user():
        """
        Extract and validate the current user from the Authorization header.
        Returns User object if valid, None otherwise.
        """
        auth = request.headers.get("Authorization", "")
        parts = auth.split()
        if len(parts) == 2 and parts[0].lower() == "bearer":
            data = verify_token(parts[1])
            if data and (uid := data.get("uid")):
                user = User.query.get(uid)
                if user:
                    return user
        return None

    def get_report_or_404(ticket: str):
        """Fetch a report by ticket or return None if not found."""
        return Report.query.filter_by(ticket=ticket).first()

    def require_code_and_report(ticket: str):
        """Verify report access using access code."""
        code = request.args.get("code", "") or request.headers.get("X-Access-Code", "")
        rpt = get_report_or_404(ticket)
        if not rpt:
            return None, jsonify({"error": "Not found"}), 404
        if not code or not verify_code(code, rpt.code_hash):
            return None, jsonify({"error": "Forbidden"}), 403
        return rpt, None, None

    # -----------------------
    # Health Check
    # -----------------------
    @app.get("/api/v1/health")
    def health_check():
        """Health check endpoint to verify server is running"""
        return jsonify({
            "status": "healthy",
            "message": "SlugLime backend is running",
            "version": "1.0.0"
        }), 200

    # -----------------------
    # Auth Routes
    # -----------------------
    @app.post("/api/v1/auth/register")
    def register():
        payload = request.get_json(silent=True) or {}
        errors = RegisterSchema().validate(payload)
        if errors:
            return jsonify({"errors": errors}), 400

        # Check if user already exists
        if User.query.filter_by(email=payload["email"].lower()).first():
            return jsonify({"error": "Email already registered"}), 400

        # Create new user
        user = User(
            email=payload["email"].lower(),
            name=payload["name"],
            password_hash=generate_password_hash(payload["password"]),
            avatar_url=None,
            verified=False,
        )
        db.session.add(user)
        db.session.commit()

        token = issue_token({"uid": user.id})
        return jsonify({"token": token, "user": UserPublicSchema().dump(user)}), 201

    @app.post("/api/v1/auth/login")
    def login():
        payload = request.get_json(silent=True) or {}
        errors = LoginSchema().validate(payload)
        if errors:
            return jsonify({"errors": errors}), 400

        user = User.query.filter_by(email=payload["email"].lower()).first()
        if not user or not check_password_hash(user.password_hash, payload["password"]):
            return jsonify({"error": "Invalid credentials"}), 401

        token = issue_token({"uid": user.id})
        return jsonify({"token": token, "user": UserPublicSchema().dump(user)}), 200

    # -----------------------
    # Feed Routes
    # -----------------------
    @app.get("/api/v1/feed")
    def get_feed():
        user = get_current_user()
        posts = Post.query.order_by(Post.created_at.desc()).limit(20).all()
        items = []
        for p in posts:
            like_count = len(p.likes)
            comment_count = len(p.comments)
            liked = False
            saved = False
            if user:
                liked = any(l.user_id == user.id for l in p.likes)
                saved = any(s.user_id == user.id for s in p.saves)
            items.append({
                "id": p.id,
                "caption": p.caption,
                "image_url": p.image_url,
                "created_at": p.created_at.isoformat(),
                "author": {
                    "id": p.author.id,
                    "email": p.author.email,
                    "name": p.author.name,
                    "avatar_url": p.author.avatar_url,
                    "verified": p.author.verified,
                },
                "like_count": like_count,
                "comment_count": comment_count,
                "liked": liked,
                "saved": saved,
            })
        return jsonify({"posts": items}), 200

    @app.post("/api/v1/posts")
    def create_post():
        user = get_current_user()
        if not user:
            return jsonify({"error": "Unauthorized"}), 401
        payload = request.get_json(silent=True) or {}
        image_url = (payload.get("image_url") or "").strip()
        caption = (payload.get("caption") or "").strip()
        if not image_url:
            return jsonify({"error": "image_url required"}), 400
        p = Post(user_id=user.id, image_url=image_url, caption=caption)
        db.session.add(p)
        db.session.commit()
        return jsonify({"id": p.id}), 201

    @app.post("/api/v1/posts/<int:post_id>/like")
    def like_post(post_id: int):
        user = get_current_user()
        if not user:
            return jsonify({"error": "Unauthorized"}), 401

        post = Post.query.get_or_404(post_id)
        existing = Like.query.filter_by(post_id=post.id, user_id=user.id).first()
        if existing:
            db.session.delete(existing)
            db.session.commit()
            liked = False
        else:
            like = Like(post_id=post.id, user_id=user.id)
            db.session.add(like)
            db.session.commit()
            liked = True

        return jsonify({"liked": liked, "like_count": len(post.likes)}), 200

    @app.post("/api/v1/posts/<int:post_id>/save")
    def save_post(post_id: int):
        user = get_current_user()
        if not user:
            return jsonify({"error": "Unauthorized"}), 401

        post = Post.query.get_or_404(post_id)
        existing = Save.query.filter_by(post_id=post.id, user_id=user.id).first()
        if existing:
            db.session.delete(existing)
            db.session.commit()
            saved = False
        else:
            s = Save(post_id=post.id, user_id=user.id)
            db.session.add(s)
            db.session.commit()
            saved = True

        return jsonify({"saved": saved}), 200

    @app.post("/api/v1/posts/<int:post_id>/comments")
    def add_comment(post_id: int):
        user = get_current_user()
        if not user:
            return jsonify({"error": "Unauthorized"}), 401
        body = (request.get_json(silent=True) or {}).get("body", "").strip()
        if not body:
            return jsonify({"error": "Body required"}), 400

        post = Post.query.get_or_404(post_id)
        c = Comment(post_id=post.id, user_id=user.id, body=body)
        db.session.add(c)
        db.session.commit()
        return jsonify({
            "comment": CommentPublicSchema().dump(c),
            "comment_count": len(post.comments)
        }), 201

    # -----------------------
    # Report Routes
    # -----------------------
    @app.get("/api/v1/reports/public")
    def get_public_reports():
        """Get public whistleblower reports for the main feed"""
        reports = Report.query.filter_by(status="open").order_by(Report.created_at.desc()).limit(20).all()

        items = []
        for rpt in reports:
            items.append({
                "id": f"report_{rpt.id}",
                "type": "report",
                "ticket": rpt.ticket,
                "title": rpt.title,
                "category": rpt.category,
                "body": rpt.body[:200] + "..." if len(rpt.body) > 200 else rpt.body,
                "created_at": rpt.created_at.isoformat(),
                "author": {
                    "id": None,
                    "email": None,
                    "name": "Anonymous Whistleblower",
                    "avatar_url": "https://via.placeholder.com/40x40/ffd700/000000?text=W",
                    "verified": True,
                },
                "like_count": 0,
                "comment_count": len(rpt.messages),
                "liked": False,
                "saved": False,
                "status": rpt.status,
            })

        return jsonify({"reports": items}), 200

    @app.post("/api/v1/reports")
    def create_report():
        # Accept JSON or multipart/form-data (from the frontend using FormData)
        payload = request.get_json(silent=True)
        if payload is None:
            # fallback to form fields for multipart/form-data
            payload = {k: v for k, v in request.form.items()}

        errors = ReportCreateSchema().validate(payload)
        if errors:
            return jsonify({"errors": errors}), 400

        ticket = gen_ticket_id()
        code = gen_access_code()

        rpt = Report(
            ticket=ticket,
            title=payload["title"].strip(),
            category=payload.get("category", "").strip() or None,
            body=payload["body"].strip(),
            code_hash=hash_code(code),
        )
        db.session.add(rpt)
        db.session.commit()

        # Save any uploaded files (optional - filenames prefixed with ticket)
        upload_folder = app.config.get("UPLOAD_FOLDER")
        for fkey in request.files:
            f = request.files.get(fkey)
            if f and getattr(f, 'filename', None):
                filename = secure_filename(f.filename)
                dest = os.path.join(upload_folder, f"{ticket}_{filename}")
                try:
                    f.save(dest)
                except Exception:
                    # ignore file save errors for now, but could log in the future
                    pass

        return jsonify({"ticket": ticket, "access_code": code}), 201

    @app.get("/api/v1/reports/<ticket>")
    def get_report(ticket: str):
        """Get a specific report by ticket (requires access code)"""
        rpt, err_resp, err_code = require_code_and_report(ticket)
        if err_resp:
            return err_resp, err_code
        
        return jsonify(ReportPublicSchema().dump(rpt)), 200

    @app.post("/api/v1/reports/<ticket>/messages")
    def post_report_message(ticket: str):
        """Post a message to a report (requires access code)"""
        rpt, err_resp, err_code = require_code_and_report(ticket)
        if err_resp:
            return err_resp, err_code
        
        payload = request.get_json(silent=True) or {}
        errors = MessageCreateSchema().validate(payload)
        if errors:
            return jsonify({"errors": errors}), 400

        msg = Message(
            report_id=rpt.id,
            body=payload["body"].strip(),
            author="user"
        )
        db.session.add(msg)
        db.session.commit()

        return jsonify({"message": "Message posted", "id": msg.id}), 201

    # -----------------------
    # Error Handlers
    # -----------------------
    @app.errorhandler(500)
    def internal_error(error):
        """Handle internal server errors"""
        app.logger.error(f'Server Error: {error}')
        return jsonify({
            "error": "Internal server error",
            "message": "The server encountered an internal error. Please check the server logs."
        }), 500

    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors"""
        return jsonify({"error": "Not found"}), 404

    @app.errorhandler(Exception)
    def handle_exception(e):
        """Handle uncaught exceptions"""
        app.logger.error(f'Unhandled Exception: {e}', exc_info=True)
        return jsonify({
            "error": "An unexpected error occurred",
            "message": str(e) if app.debug else "Please contact support"
        }), 500

    return app


def main():
    """Main entry point with environment checks"""
    import sys
    
    # Check Python version
    if sys.version_info < (3, 10):
        print("ERROR: Python 3.10 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    
    # Check if SECRET_KEY is set
    if not os.getenv("SECRET_KEY"):
        print("WARNING: SECRET_KEY not set in environment")
        print("Using a randomly generated key (tokens will be invalidated on restart)")
    
    # Get host and port from config
    from config import Config
    host = Config.FLASK_HOST
    port = Config.FLASK_PORT
    
    print("="*60)
    print("Starting SlugLime Backend Server")
    print("="*60)
    print(f"Python version: {sys.version.split()[0]}")
    try:
        from importlib.metadata import version
        print(f"Flask version: {version('flask')}")
    except:
        print("Flask version: 3.0.3")
    print(f"Server: http://{host}:{port}")
    print("="*60)
    
    try:
        app = create_app()
        # Use debug=False to avoid reloader path issues on Windows
        app.run(host=host, port=port, debug=False)
    except Exception as e:
        print(f"\nERROR: Failed to start server: {e}")
        print("\nTroubleshooting:")
        print("1. Check if port 5000 is already in use")
        print("2. Verify .env file exists and has SECRET_KEY set")
        print("3. Run: python check_setup.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
