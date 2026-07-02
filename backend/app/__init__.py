from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Rent & Flatmate Finder Backend Running Successfully!"

    return app