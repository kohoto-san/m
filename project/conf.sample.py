import os
from .settings import BASE_DIR

#   Database credentials
db = dict(
    ENGINE='django.db.backends.sqlite3',
    NAME=os.path.join(BASE_DIR, 'db.sqlite3'),
)

SECRET_KEY = 'SECRET_KEY'

# set to 'production'
env = 'local'
