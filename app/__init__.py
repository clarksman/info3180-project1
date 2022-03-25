from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

UPLOAD_FOLDER = './app/uploads'
app = Flask(__name__)
app.config.from_object(Config)

app.secret_key='Som3$ec5etK*y'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Lornason50022@localhost/project1'
app.config["UPLOAD_FOLDER"]  = UPLOAD_FOLDER
from app import views

