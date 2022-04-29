"""App.py is the main flask app.  This handles the routing and
pulling of data needed for index.html"""
import os
from dotenv import find_dotenv, load_dotenv
import flask
from flask_login import (
    LoginManager,
    login_required,
    current_user,
    login_user,
    logout_user,
)
from movie_api import get_movie_titles, media_wiki, movie_img, movie_info
from movie_db import User, Reviews, db

load_dotenv(find_dotenv())

app = flask.Flask(__name__)

# To point SQLAlchemy to your Heroku db
app.config["SQLALCHEMY_DATABASE_URL"] = os.getenv("DATABASE_URL")
# Gets rid of warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

db.init_app(app)
with app.app_context():
    db.create_all()


login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """Loads the user object from the user id found in the session"""
    return User.query.get(int(user_id))


@app.route("/")
@login_required
def index():
    """Gets a list of movies to show on index.html"""
    flask.session.pop("_flashes", None)
    movies = get_movie_titles()

    return flask.render_template(
        "index.html",
        movies=movies,
    )


@app.route("/movie")
@login_required
def movie():
    """Calls the movieAPI.py functions and passes the data to the index.html"""
    flask.session.pop("_flashes", None)
    movie_id = flask.request.args.get("movie_id")
    movies = movie_info(movie_id)
    imgs = movie_img(movie_id)
    search_wiki = media_wiki(movie_id)
    revs = Reviews.get_reviews(Reviews, movie_id)

    genre = ""
    for i in range(len(movies["genres"])):
        genre += movies["genres"][i]["name"] + ", "

    genre = genre.rstrip(", ")

    return flask.render_template(
        "movie.html",
        movie=movies,
        imageURL=imgs,
        results=search_wiki,
        genre=genre,
        movie_id=movie_id,
        reviews=revs,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login method"""
    if flask.request.method == "GET":
        return flask.render_template("login.html")
    else:
        username = flask.request.form.get("username")
        password = flask.request.form.get("password")
        if flask.request.form.get("remember"):
            remember = True
        else:
            remember = False

        user = User.signin(User, username, password)
        if user == 1:
            flask.session.pop("_flashes", None)
            flask.flash("Please sign up first!")
            return flask.redirect(flask.url_for("signup"))
        elif user == 2:
            flask.session.pop("_flashes", None)
            flask.flash("Login information is incorrect.  Please try again")
            return flask.redirect(flask.url_for("login"))

        login_user(user, remember=remember)
        flask.session.pop("_flashes", None)
        return flask.redirect(flask.url_for("index"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Signup Method"""
    if flask.request.method == "GET":
        return flask.render_template("signup.html")
    else:
        username = flask.request.form.get("username")
        password = flask.request.form.get("password")
        confirm_pwd = flask.request.form.get("confirm_pwd")
        if confirm_pwd != password:
            flask.session.pop("_flashes", None)
            flask.flash("Passwords did not match")
            return flask.redirect(flask.url_for("signup"))
        user = User.query.filter_by(username=username).first()
        if user:
            flask.session.pop("_flashes", None)
            flask.flash("Username already exists")
            return flask.redirect(flask.url_for("signup"))
        User.signup(user, username, password)
        flask.session.pop("_flashes", None)
        return flask.redirect(flask.url_for("login"))


@app.route("/logout")
@login_required
def logout():
    """Logout method"""
    logout_user()
    return flask.redirect(flask.url_for("index"))


@app.route("/addReview", methods=["POST"])
@login_required
def add_review():
    """User is adding a review to a movie"""
    movie_id = flask.request.form.get("movie_id")
    user_id = current_user.get_id()
    review = flask.request.form.get("review")
    rating = flask.request.form.get("rating")

    Reviews.save_review(Reviews, movie_id, user_id, review, rating)
    flask.flash("Review submitted")
    return flask.redirect(flask.url_for("movie", movie_id=movie_id))


app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT")), debug=True)
