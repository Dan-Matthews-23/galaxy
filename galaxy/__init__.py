import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt  # 1. Add this import

if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)

# Security Key
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev_key_only_for_local")

# Database Configuration
# This looks for a DB_URL; if it doesn't find one, it creates a local 'galaxy.db' file.
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL", "sqlite:///galaxy.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)  # 2. Initialize it here

from galaxy import routes, models  # noqa