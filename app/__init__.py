__author__ = 'pepo'

from flask import Flask
from Flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

from app import views
