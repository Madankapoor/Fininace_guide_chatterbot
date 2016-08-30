WTF_CSRF_ENABLED = True
SECRET_KEY = '12849080192@!#459jhfaldfh2191!@3849a@#hof89iqokzxc#$vn--=-=-=-===kasdjjkhasdklfjhajksdfhjkasdhfkjasd'
TEMPLATES_AUTO_RELOAD = False
SQLALCHEMY_TRACK_MODIFICATIONS =False
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

MAIL_SERVER='smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'finchatbot@gmail.com'
MAIL_PASSWORD = '52473611'
MAIL_USE_SSL = True