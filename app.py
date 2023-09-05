"""Flask app for Notes"""

import os
from flask import Flask, render_template, flash, redirect, jsonify, request, session
# from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User
# from sqlalchemy.exc import  DataError
from forms import AddNewUserForm, LoginForm, CSRFProtectForm


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///notes")


connect_db(app)

# CSRF_FORM = CSRFProtectForm()


@app.get('/')
def redirect_to_register():
    """Redirect to register page"""

    return redirect('/register')

#Authorization Routes

@app.route('/register', methods=['GET', 'POST'])
def handle_registration():
    """Show and handle registration form."""

    #Guard for already logged in
    if session.get("username"):
        return redirect(f"/users/{session['username']}")

    form = AddNewUserForm()

    if form.validate_on_submit():
        #Guards for duplicate username/email
        unique_value_conflict = False
        if User.query.filter_by(username=form.username.data).one_or_none():
            form.username.errors = ["Username already in use"]
            unique_value_conflict = True

        if User.query.filter_by(email=form.email.data).one_or_none():
            form.email.errors = ["Email already in use"]
            unique_value_conflict = True

        if unique_value_conflict:
            return render_template('add_user_form.html', form=form)

        user = User.register(
            username = form.username.data,
            password = form.password.data,
            email = form.email.data,
            first_name = form.first_name.data,
            last_name = form.last_name.data
        )



        db.session.add(user)
        db.session.commit()

        session["username"] = user.username

        flash(f"Welcome {user.username}")
        return redirect(f'/users/{user.username}')

    else:
        return render_template('add_user_form.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def handle_login():
    """Show and handle registration form."""

    #Guard for already logged in
    if session.get("username"):
        return redirect(f"/users/{session['username']}")

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(
            username = form.username.data,
            password = form.password.data
        )

        if user:
            session["username"] = user.username
            flash(f"Login Succesful")
            return redirect(f'/users/{user.username}')
        else:
            form.password.errors = ["Incorrect username/password"]


    return render_template('login_form.html', form=form)


@app.post("/logout")
def logout_user():
    """Logout user and redirect to home page"""

    form = CSRFProtectForm()

    if form.validate_on_submit():
        # Remove "user_id" if present, but no errors if it wasn't
        session.pop("username", None)
        flash("Logout successful")
        return redirect("/")


#User Routes

@app.get("/users/<username>")
def show_user_info(username):
    """Shows information to logged-in user"""

    user = User.query.get_or_404(username)

    form = CSRFProtectForm()

    if session.get("username") == username:
        return render_template("user_details.html", user=user, form=form)

    else:
        flash("You must be logged in to see user page")
        return redirect("/login")
