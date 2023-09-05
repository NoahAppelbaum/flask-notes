"""Forms for Notes app."""

from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class AddNewUserForm(FlaskForm):
    """Form for adding new user"""

    username = StringField("Username",
                           validators=[InputRequired(), Length(max=20)])
    password = PasswordField("Password",
                           validators=[InputRequired(), Length(max=30)])
    email = EmailField("email",
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
                           validators=[InputRequired(), Length(max=30)])
