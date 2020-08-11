from flask import Flask
from config import Config

# import for Flask DB and Migrator
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app= Flask(__name__)

app.config.from_object(Config)  # pulling in our config calss

db= SQLAlchemy(app)
migrate = Migrate(app,db)


from avengers_phonebook import routes 
from avengers_phonebook import models