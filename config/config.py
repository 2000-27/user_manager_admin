import os
from dotenv import load_dotenv

from pathlib import Path

load_dotenv()
base_dir = os.path.abspath(os.path.dirname(__file__))
class DevConfig(object):
    TESTING = False
    print("base_dir ==== ",base_dir)
    SQLALCHEMY_DATABASE_URI = base_dir+"sqlite:////data.db"
    SECRET_KEY = os.environ['SECRET_KEY']
