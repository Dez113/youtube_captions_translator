from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object('my_test_app.config')

db.init_app(app)

from my_test_app import views#, models
