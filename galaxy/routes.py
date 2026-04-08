from flask import render_template, url_for, flash, redirect, request
from galaxy import app, db, bcrypt
from galaxy.forms import RegistrationForm, LoginForm # Add LoginForm
from galaxy.models import User
from flask_login import login_user, current_user, logout_user, login_required # Add these



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
        db.session.flush() # This 'pre-saves' the user to get their ID for the next steps


        #Add these values to all models upon registration (income, attack, defense)      
        #starting_income = Income(owner=user, credits=1000, crystal_ore=500)
        #starting_military = Military(owner=user, fleet_size=5)

        #db.session.add(starting_income)
        #db.session.add(starting_military)
        
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('home'))
        
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    # If they are already logged in, send them to the home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        # Check if user exists AND if the password matches the hash
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            
            # If the user tried to access a protected page before logging in,
            # this takes them back there after they log in
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
            
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/dashboard")
@login_required # This forces the user to log in before seeing this page
def dashboard():
    return render_template('dashboard.html', title='Dashboard')