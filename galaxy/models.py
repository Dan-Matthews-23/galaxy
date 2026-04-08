from galaxy import db, login_manager # <--- Add login_manager here
from flask_login import UserMixin # Import the mixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin): # Add UserMixin here
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # 60 characters is standard for a hashed password (Bcrypt)
    password = db.Column(db.String(60), nullable=False)

    ### RELATIONSHIP POINTERS (Commented out until tables are built) ###
    # income = db.relationship('Income', backref='owner', uselist=False)
    # military = db.relationship('Military', backref='owner', uselist=False)
    # exploration = db.relationship('Exploration', backref='owner', uselist=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"