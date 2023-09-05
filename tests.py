import os

os.environ["DATABASE_URL"] = 'postgresql:///notes_test'

from unittest import TestCase

from app import app

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

db.drop_all()
db.create_all()
