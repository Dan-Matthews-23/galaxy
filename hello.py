from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_galaxy():
    return "<h1>Welcome to the Milky Way.</p>"