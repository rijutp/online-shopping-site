from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#Create an Instance of Flask
app = Flask(__name__)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# app.run(debug = "TRUE", host= "0.0.0.0", port= 5000)
#Include config from config.py
app.config.from_object('config')
app.secret_key = 'some_secret'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#Create an instance of SQLAclhemy
db = SQLAlchemy(app)
from app import views, models