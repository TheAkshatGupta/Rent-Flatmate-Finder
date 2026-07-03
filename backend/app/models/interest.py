from extensions import db


class Interest(db.Model):

    __tablename__ = "interests"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, nullable=False)

    listing_id = db.Column(db.Integer, nullable=False)

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )