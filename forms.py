"""Forms for Notes app."""

from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length

class AddNewUserForm(FlaskForm):
    """Form for adding new user"""

    username = StringField("Username",
                           validators=[InputRequired(), Length(max=20)])
    password = PasswordField("Password",
                           validators=[InputRequired(), Length(max=100)])
    email = EmailField("Email",
                       validators=[InputRequired(), Length(max=50)])
    first_name = StringField("First Name",
                             validators=[InputRequired(), Length(max=30)])
    last_name = StringField("Last Name",
                            validators=[InputRequired(), Length(max=30)])


class LoginForm(FlaskForm):
    """Form for user login"""

    username = StringField("Username",
                           validators=[InputRequired(), Length(max=20)])
    password = PasswordField("Password",
                           validators=[InputRequired(), Length(max=100)])

class CSRFProtectForm(FlaskForm):
    """Form for CSRF protection"""
