from flask import Flask

from config import Config
from extensions import db, login_manager

# Import Models
from app.models.user import User

# Import Routes
from app.routes.auth import auth_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize Extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Home Route
    @app.route("/")
    def home():
        return "<h1>Rent & Flatmate Finder Backend Running Successfully 🚀</h1>"

    # Register Blueprint
    app.register_blueprint(auth_bp)

    # Create Tables
    with app.app_context():
        db.create_all()

    # Debug Routes
    print("\n================ ROUTES ================\n")
    print(app.url_map)
    print("\n========================================\n")

    return app