from extensions import db


class Profile(db.Model):

    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, nullable=False)

    age = db.Column(db.Integer, nullable=False)

    gender = db.Column(db.String(20), nullable=False)

    occupation = db.Column(db.String(100), nullable=False)

    budget = db.Column(db.Float, nullable=False)

    food_preference = db.Column(db.String(50), nullable=False)

    smoking = db.Column(db.String(20), nullable=False)

    drinking = db.Column(db.String(20), nullable=False)

    pets = db.Column(db.String(20), nullable=False)

    sleep_schedule = db.Column(db.String(50), nullable=False)

    cleanliness = db.Column(db.String(50), nullable=False)

    languages = db.Column(db.String(200), nullable=False)

    bio = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )