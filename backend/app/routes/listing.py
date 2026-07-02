from flask import Blueprint, request, jsonify

from extensions import db
from app.models.listing import Listing

listing_bp = Blueprint("listing", __name__)


# -----------------------
# Add Listing
# -----------------------
@listing_bp.route("/listings", methods=["POST"])
def add_listing():

    data = request.get_json()

    required = [
        "title",
        "description",
        "rent",
        "city",
        "area",
        "property_type",
        "owner_name",
        "owner_phone"
    ]

    for field in required:
        if field not in data:
            return jsonify({
                "message": f"{field} is required"
            }), 400

    listing = Listing(

        title=data["title"],
        description=data["description"],
        rent=data["rent"],
        city=data["city"],
        area=data["area"],
        property_type=data["property_type"],
        owner_name=data["owner_name"],
        owner_phone=data["owner_phone"]

    )

    db.session.add(listing)
    db.session.commit()

    return jsonify({
        "message": "Listing Added Successfully"
    }), 201


# -----------------------
# Get All Listings
# -----------------------
@listing_bp.route("/listings", methods=["GET"])
def get_all_listings():

    listings = Listing.query.all()

    result = []

    for listing in listings:

        result.append({

            "id": listing.id,

            "title": listing.title,

            "description": listing.description,

            "rent": listing.rent,

            "city": listing.city,

            "area": listing.area,

            "property_type": listing.property_type,

            "owner_name": listing.owner_name,

            "owner_phone": listing.owner_phone,

            "available": listing.available

        })

    return jsonify(result), 200


# -----------------------
# Get Single Listing
# -----------------------
@listing_bp.route("/listings/<int:id>", methods=["GET"])
def get_listing(id):

    listing = Listing.query.get(id)

    if not listing:

        return jsonify({
            "message": "Listing not found"
        }), 404

    return jsonify({

        "id": listing.id,

        "title": listing.title,

        "description": listing.description,

        "rent": listing.rent,

        "city": listing.city,

        "area": listing.area,

        "property_type": listing.property_type,

        "owner_name": listing.owner_name,

        "owner_phone": listing.owner_phone,

        "available": listing.available

    }), 200
# -----------------------
# Update Listing
# -----------------------
@listing_bp.route("/listings/<int:id>", methods=["PUT"])
def update_listing(id):

    listing = Listing.query.get(id)

    if not listing:
        return jsonify({"message": "Listing not found"}), 404

    data = request.get_json()

    listing.title = data.get("title", listing.title)
    listing.description = data.get("description", listing.description)
    listing.rent = data.get("rent", listing.rent)
    listing.city = data.get("city", listing.city)
    listing.area = data.get("area", listing.area)
    listing.property_type = data.get("property_type", listing.property_type)
    listing.owner_name = data.get("owner_name", listing.owner_name)
    listing.owner_phone = data.get("owner_phone", listing.owner_phone)
    listing.available = data.get("available", listing.available)

    db.session.commit()

    return jsonify({
        "message": "Listing Updated Successfully"
    }), 200


# -----------------------
# Delete Listing
# -----------------------
@listing_bp.route("/listings/<int:id>", methods=["DELETE"])
def delete_listing(id):

    listing = Listing.query.get(id)

    if not listing:
        return jsonify({
            "message": "Listing not found"
        }), 404

    db.session.delete(listing)
    db.session.commit()

    return jsonify({
        "message": "Listing Deleted Successfully"
    }), 200
# -----------------------
# Search & Filter Listings
# -----------------------
@listing_bp.route("/listings/search", methods=["GET"])
def search_listings():

    city = request.args.get("city")
    property_type = request.args.get("property_type")
    max_rent = request.args.get("max_rent")

    query = Listing.query

    if city:
        query = query.filter(Listing.city.ilike(f"%{city}%"))

    if property_type:
        query = query.filter(
            Listing.property_type.ilike(f"%{property_type}%")
        )

    if max_rent:
        query = query.filter(
            Listing.rent <= float(max_rent)
        )

    listings = query.all()

    result = []

    for listing in listings:

        result.append({

            "id": listing.id,
            "title": listing.title,
            "description": listing.description,
            "rent": listing.rent,
            "city": listing.city,
            "area": listing.area,
            "property_type": listing.property_type,
            "owner_name": listing.owner_name,
            "owner_phone": listing.owner_phone,
            "available": listing.available

        })

    return jsonify(result), 200