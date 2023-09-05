"""Forms for Notes app."""

from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import InputRequired, Length, Email

class AddNewUser(FlaskForm):
    """Form for adding new user"""

    username = StringField("Username",
                           validators=[InputRequired(), Length(max=20)])
    password = StringField("Password",
                           validators=[InputRequired(), Length(max=30)])
    email = EmailField("email",
                       validators=[InputRequired(), Length(max=50)])
    first_name = StringField("First Name",
                             validators=[InputRequired(), Length(max=30)])
    last_name = StringField("Last Name",
                            validators=[InputRequired(), Length(max=30)])
