WTF_CSRF_ENABLED = True
SECRET_KEY = '12849080192@!#459jhfaldfh2191!@3849a@#hof89iqokzxc#$vn--=-=-=-===kasdjjkhasdklfjhajksdfhjkasdhfkjasd'
TEMPLATES_AUTO_RELOAD = True
SQLALCHEMY_TRACK_MODIFICATIONS =False
import os
basedir = os.path.abspath(os.path.dirname(__file__))
Heroku = os.environ.get('HEROKU')

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_RECORD_QUERIES = True
    
     
MAIL_SERVER='smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'finchatbot@gmail.com'
MAIL_PASSWORD = '52473611'
MAIL_USE_SSL = True