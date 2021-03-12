from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager

from .config import Config
from .models import db

#Initialize application
app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'auth.unauthorized'

app.config.from_object(Config)

#Set up db
db.init_app(app)
Migrate(app, db)



@app.route('/')
def hello():
    return (
        'Hello world!'
    )