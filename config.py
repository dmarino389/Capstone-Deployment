import os

# basedir = os.path.abspath(os.path.dirname(__name__))

class Config():
  FLASK_APP = os.environ.get("FLASK_APP")
  FLASK_DEBUG = os.environ.get("FLASK_DEBUG")
  SECRET_KEY = os.environ.get("SECRET_KEY")
  # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  SQLALCHEMY_DATABASE_URI = 'postgres://hpawltfl:y5MqwxxP2LT0qR3hzR1jBPgVAohkckYJ@jelani.db.elephantsql.com/hpawltfl'
  SQLALCHEMY_TRACK_MODIFICATIONS = False