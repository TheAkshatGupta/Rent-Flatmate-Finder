from flask import Blueprint, jsonify

from extensions import db

from app.models.profile import Profile
from app.models.listing import Listing
from app.models.compatibility import Compatibility

from app.services.compatibility_service import calculate_score
from app.services.gemini_service import get_ai_compatibility

compatibility_bp = Blueprint(
    "compatibility",
    __name__
)


@compatibility_bp.route(
    "/compatibility/<int:user_id>/<int:listing_id>",
    methods=["GET"]
)
def compatibility(user_id, listing_id):

    profile = Profile.query.filter_by(
        user_id=user_id
    ).first()

    listing = Listing.query.get(
        listing_id
    )

    if not profile or not listing:

        return jsonify({
            "message": "Data not found"
        }), 404

    # Try Gemini first
    result = get_ai_compatibility(
        profile,
        listing
    )

    # Fallback
    if result is None:

        result = calculate_score(
            profile,
            listing
        )

    existing = Compatibility.query.filter_by(
        user_id=user_id,
        listing_id=listing_id
    ).first()

    if existing:

        existing.score = result["score"]
        existing.explanation = result["explanation"]

    else:

        db.session.add(

            Compatibility(

                user_id=user_id,
                listing_id=listing_id,
                score=result["score"],
                explanation=result["explanation"]

            )

        )

    db.session.commit()

    return jsonify(result), 200