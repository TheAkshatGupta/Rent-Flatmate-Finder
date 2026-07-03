from flask import Flask

from config import Config
from extensions import db, login_manager

# Models
from app.models import (
    User,
    Listing,
    Profile,
    Interest,
    Message,
    Compatibility
)

# Routes
from app.routes.auth import auth_bp
from app.routes.listing import listing_bp
from app.routes.profile import profile_bp
from app.routes.interest import interest_bp
from app.routes.chat import chat_bp
from app.routes.compatibility import compatibility_bp


def create_app():

    app = Flask(__name__)

    # Configuration
    app.config.from_object(Config)

    # Initialize Extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Home Route
    @app.route("/")
    def home():
        return "<h1>Rent & Flatmate Finder Backend Running Successfully 🚀</h1>"

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(listing_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(interest_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(compatibility_bp)

    # Create Database Tables
    with app.app_context():
        db.create_all()

    return app