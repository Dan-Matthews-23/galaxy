
from galaxy import app
from flask import render_template, url_for, flash, redirect
from galaxy.forms import RegistrationForm

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # This checks if the user clicked 'Submit' AND if the data is valid
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    
    return render_template('register.html', title='Register', form=form)