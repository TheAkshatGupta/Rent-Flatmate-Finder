from flask import Blueprint, request, jsonify

from extensions import db
from app.models.interest import Interest

interest_bp = Blueprint("interest", __name__)


@interest_bp.route("/interest", methods=["POST"])
def send_interest():

    data = request.get_json()

    interest = Interest(

        user_id=data["user_id"],
        listing_id=data["listing_id"]

    )

    db.session.add(interest)
    db.session.commit()

    return jsonify({

        "message": "Interest Sent Successfully"

    }), 201


@interest_bp.route("/interest", methods=["GET"])
def get_interests():

    interests = Interest.query.all()

    result = []

    for interest in interests:

        result.append({

            "id": interest.id,
            "user_id": interest.user_id,
            "listing_id": interest.listing_id,
            "status": interest.status

        })

    return jsonify(result), 200