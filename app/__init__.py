from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from .config import DevConfig

db = SQLAlchemy()
ma = Marshmallow()

app = Flask(__name__)
from  .routes import new_mold,second
app.config.from_object(DevConfig)


app.register_blueprint(new_mold, url_prefix='/api')
app.register_blueprint(second, url_prefix='/api')
db.init_app(app)   
