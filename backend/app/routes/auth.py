from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db
from app.models.user import User

auth_bp = Blueprint("auth", __name__)


# -----------------------------
# Register API
# -----------------------------
@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    if not data:
        return jsonify({"message": "No data received"}), 400

    required_fields = [
        "full_name",
        "email",
        "password",
        "role"
    ]

    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({
                "message": f"{field} is required"
            }), 400

    existing_user = User.query.filter_by(email=data["email"]).first()

    if existing_user:
        return jsonify({
            "message": "Email already exists"
        }), 409

    new_user = User(
        full_name=data["full_name"],
        email=data["email"],
        password=generate_password_hash(data["password"]),
        role=data["role"],
        phone=data.get("phone")
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "Registration Successful"
    }), 201


# -----------------------------
# Login API
# -----------------------------
@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "No data received"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "message": "Email and Password are required"
        }), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({
            "message": "Invalid Email"
        }), 404

    if not check_password_hash(user.password, password):
        return jsonify({
            "message": "Invalid Password"
        }), 401

    return jsonify({
        "message": "Login Successful",
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role
        }
    }), 200