import os
from flask import Flask, render_template, flash, redirect, jsonify, request
# from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, DEFAULT_IMAGE_URL
# from sqlalchemy.exc import  DataError
from forms import

"""Flask app for Cupcakes"""
app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///notes")


connect_db(app)
