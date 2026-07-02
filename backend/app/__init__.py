from flask import Flask

from config import Config
from app.models import User
from extensions import db, login_manager


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    login_manager.init_app(app)

    @app.route("/")
    def home():
        return "<h1>Rent & Flatmate Finder Backend Running Successfully 🚀</h1>"

    with app.app_context():
        db.create_all()

    return app