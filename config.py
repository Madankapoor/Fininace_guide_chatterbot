WTF_CSRF_ENABLED = True
SECRET_KEY = '1239080192@!#459jhfaldfh2191!@3849a@#hof89iqokzxc#$vn--=-=-=-===kasdjjkhasdklfjhajksdfhjkasdhfkjasd'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')