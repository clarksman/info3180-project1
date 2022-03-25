import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:Lornason50022@localhost/project1')

    #SQLALCHEMY_DATABASE_URI = "postgresql://hribhbnfdumafr:a7c5c75428c7c9fa82b8c2a0b5b25e76dcb2fc4d72c7c139428be6b3c605fcd0@ec2-52-71-217-158.compute-1.amazonaws.com:5432/dbt30aga3brhsl"
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed