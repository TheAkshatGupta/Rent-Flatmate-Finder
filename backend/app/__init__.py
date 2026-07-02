from flask import Flask

from config import Config
from extensions import db, login_manager

# Import models
from app.models import User

# Import routes
from app.routes.auth import auth_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app