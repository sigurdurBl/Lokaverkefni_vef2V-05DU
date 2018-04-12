import json
from flask import *
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("hmoe.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/games")
def games():
    return render_template("game.html")

@app.route("/series")
def series():
    return render_template("series.html")

app.run()
