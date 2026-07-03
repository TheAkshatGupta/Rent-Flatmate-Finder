from extensions import db


class Compatibility(db.Model):

    __tablename__ = "compatibility"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, nullable=False)

    listing_id = db.Column(db.Integer, nullable=False)

    score = db.Column(db.Integer, nullable=False)

    explanation = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )