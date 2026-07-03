from flask import Blueprint, request, jsonify

from extensions import db
from app.models.profile import Profile

profile_bp = Blueprint("profile", __name__)


# -----------------------
# Create Profile
# -----------------------
@profile_bp.route("/profile", methods=["POST"])
def create_profile():

    data = request.get_json()

    required = [
        "user_id",
        "age",
        "gender",
        "occupation",
        "budget",
        "food_preference",
        "smoking",
        "drinking",
        "pets",
        "sleep_schedule",
        "cleanliness",
        "languages"
    ]

    for field in required:
        if field not in data:
            return jsonify({
                "message": f"{field} is required"
            }), 400

    existing = Profile.query.filter_by(user_id=data["user_id"]).first()

    if existing:
        return jsonify({
            "message": "Profile already exists"
        }), 409

    profile = Profile(
        user_id=data["user_id"],
        age=data["age"],
        gender=data["gender"],
        occupation=data["occupation"],
        budget=data["budget"],
        food_preference=data["food_preference"],
        smoking=data["smoking"],
        drinking=data["drinking"],
        pets=data["pets"],
        sleep_schedule=data["sleep_schedule"],
        cleanliness=data["cleanliness"],
        languages=data["languages"],
        bio=data.get("bio")
    )

    db.session.add(profile)
    db.session.commit()

    return jsonify({
        "message": "Profile Created Successfully"
    }), 201


# -----------------------
# Get Profile
# -----------------------
@profile_bp.route("/profile/<int:user_id>", methods=["GET"])
def get_profile(user_id):

    profile = Profile.query.filter_by(user_id=user_id).first()

    if not profile:
        return jsonify({
            "message": "Profile not found"
        }), 404

    return jsonify({
        "id": profile.id,
        "user_id": profile.user_id,
        "age": profile.age,
        "gender": profile.gender,
        "occupation": profile.occupation,
        "budget": profile.budget,
        "food_preference": profile.food_preference,
        "smoking": profile.smoking,
        "drinking": profile.drinking,
        "pets": profile.pets,
        "sleep_schedule": profile.sleep_schedule,
        "cleanliness": profile.cleanliness,
        "languages": profile.languages,
        "bio": profile.bio
    }), 200


# -----------------------
# Update Profile
# -----------------------
@profile_bp.route("/profile/<int:user_id>", methods=["PUT"])
def update_profile(user_id):

    profile = Profile.query.filter_by(user_id=user_id).first()

    if not profile:
        return jsonify({
            "message": "Profile not found"
        }), 404

    data = request.get_json()

    profile.age = data.get("age", profile.age)
    profile.gender = data.get("gender", profile.gender)
    profile.occupation = data.get("occupation", profile.occupation)
    profile.budget = data.get("budget", profile.budget)
    profile.food_preference = data.get("food_preference", profile.food_preference)
    profile.smoking = data.get("smoking", profile.smoking)
    profile.drinking = data.get("drinking", profile.drinking)
    profile.pets = data.get("pets", profile.pets)
    profile.sleep_schedule = data.get("sleep_schedule", profile.sleep_schedule)
    profile.cleanliness = data.get("cleanliness", profile.cleanliness)
    profile.languages = data.get("languages", profile.languages)
    profile.bio = data.get("bio", profile.bio)

    db.session.commit()

    return jsonify({
        "message": "Profile Updated Successfully"
    }), 200