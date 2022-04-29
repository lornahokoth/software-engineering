"""movie_db.py does all the heavy lifting for pulling data
from the database."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model):
    """User table to handle the user logins"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    is_active = db.Column(db.Boolean)
    is_authenticated = db.Column(db.Boolean)

    def get_id(self):
        """get user id"""
        return self.id

    def signin(self, uname, pwd):
        """Adding a new user to the User database"""
        user = User.query.filter_by(username=uname).first()
        if not user:
            return 1
        elif not check_password_hash(user.password, pwd):
            return 2
        else:
            return user

    def signup(self, uname, pwd):
        """Adding a new user to the User database"""
        new_user = User(
            username=uname,
            password=generate_password_hash(pwd, method="sha256"),
            is_active=True,
            is_authenticated=True,
        )
        db.session.add(new_user)
        db.session.commit()

    def get_username(self, user_id):
        """Returns the username for a given user_id"""
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return "annonymous"
        else:
            return user.username


class Reviews(db.Model):
    """Reviews table to store user reviews for movies"""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    movie_id = db.Column(db.Integer)
    datetime = db.Column(db.DateTime)
    review = db.Column(db.String(500))
    rating = db.Column(db.Integer)

    def get_reviews(self, movie_id):
        """Function to pull all the reviews for a given movie"""
        reviews = Reviews.query.filter_by(movie_id=movie_id).all()
        if len(reviews) == 0:
            return ["None"]
        else:
            movie_reviews = []
            for review in reviews:
                user = User.get_username(User, review.user_id)
                rev = review.review
                rating = review.rating
                movie_reviews.append(
                    {
                        "username": user,
                        "review": rev,
                        "rating": rating,
                    }
                )
            return movie_reviews

    def save_review(self, movie_id, user_id, review, rating):
        """Save a new review for a movie"""
        now = datetime.now()
        new_movie = Reviews(
            user_id=user_id,
            movie_id=movie_id,
            datetime=now,
            review=review,
            rating=rating,
        )
        db.session.add(new_movie)
        db.session.commit()
