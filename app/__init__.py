from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy 

from config import Config

#Initialize application
app = Flask(__name__)
app.config.from_object(Config)

#Set up db
db = SQLAlchemy(app)


migrate = Migrate(app, db)



@app.route('/')
def hello():
    return (
        'Hello world!'
    )