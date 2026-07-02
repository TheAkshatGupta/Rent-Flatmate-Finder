from extensions import db


class Listing(db.Model):

    __tablename__ = "listings"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)

    description = db.Column(db.Text, nullable=False)

    rent = db.Column(db.Float, nullable=False)

    city = db.Column(db.String(100), nullable=False)

    area = db.Column(db.String(100), nullable=False)

    property_type = db.Column(db.String(50), nullable=False)

    owner_name = db.Column(db.String(100), nullable=False)

    owner_phone = db.Column(db.String(15), nullable=False)

    available = db.Column(db.Boolean, default=True)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )