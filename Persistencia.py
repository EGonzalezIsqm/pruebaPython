import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://python:prueba12345@localhost/dbpython'

db = SQLAlchemy(app)

SECRET_KEY = os.urandom(32)
# forms
CSRF_ENABLED = True


DEBUG = True