import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "rent-flatmate-secret-key")

    SQLALCHEMY_DATABASE_URI = "sqlite:///rent_flatmate.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False