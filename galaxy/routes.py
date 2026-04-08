
from galaxy import app, db, bcrypt  # <--- Make sure 'bcrypt' is added here!
from flask import render_template, url_for, flash, redirect
from galaxy.forms import RegistrationForm
from galaxy.models import User  # <--- Check if this line is missing!


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Scramble the password!
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        user = User(username=form.username.data, 
                    email=form.email.data, 
                    password=hashed_password) # Save the SCRAMBLED version
        
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('home'))
        
    return render_template('register.html', title='Register', form=form)