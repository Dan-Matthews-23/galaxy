from flask import render_template
from galaxy import app

@app.route("/")
def home():
    return render_template("index.html")