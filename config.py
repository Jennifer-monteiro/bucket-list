import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config():
	FLASK_APP = os.environ.get("FLASK_APP")
	FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
	SECRET_KEY=os.environ.get('SECRET_KEY')
	ACCESS_KEY = os.environ.get("ACCESS_KEY")
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql+psycopg2://username:password@localhost/db_name'
	SQLALCHEMY_TRACK_MODIFICATIONS = False


