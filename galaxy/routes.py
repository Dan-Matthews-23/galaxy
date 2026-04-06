from flask import render_template
from galaxy import app, db

@app.route("/")
def home():
    return "<h1>Welcome to the Galaxy</h1><p>The routing is working!</p>"