import os
from flask import Flask, render_template, flash, redirect, jsonify, request, session
# from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User
# from sqlalchemy.exc import  DataError
from forms import AddNewUserForm, LoginForm


"""Flask app for Cupcakes"""
app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///notes")


connect_db(app)


@app.get('/')
def redirect_to_register():
    """Redirect to register page"""

    return redirect('/register')

@app.route('/register', methods=['GET', 'POST'])
def handle_registration():
    """Show and handle registration form."""

    form = AddNewUserForm()

    if form.validate_on_submit():
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


@app.get("/users/<username>")
def show_user_info(username):
    """Shows information to logged-in user"""

    user = User.query.get_or_404(username)

    if session.get("username") == username:
        return render_template("user_details.html", user=user)

    else:
        return redirect("/login")
