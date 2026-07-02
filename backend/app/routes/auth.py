from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from extensions import db
from app.models.user import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    if not data:
        return jsonify({"message": "No data received"}), 400

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "Email already exists"}), 409

    new_user = User(
        full_name=data["full_name"],
        email=data["email"],
        password=generate_password_hash(data["password"]),
        role=data["role"],
        phone=data.get("phone")
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Registration Successful"}), 201