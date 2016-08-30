from flask import Flask
#Importing Libs
from flask_sqlalchemy  import SQLAlchemy
from flask_login import LoginManager 
from flask_bcrypt  import Bcrypt
from flask_mail import Mail, Message
import aiml
import os


app=Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
kernel = aiml.Kernel()
bcrypt=Bcrypt()
mail = Mail(app)

login_manager=LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

from app import views,models