import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
