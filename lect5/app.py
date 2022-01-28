import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html", name="Lornah")


app.run(debug=True)
