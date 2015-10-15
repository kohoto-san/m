import os
from .settings import BASE_DIR

#   Database credentials
db = dict(
    ENGINE='django.db.backends.sqlite3',
    NAME=os.path.join(BASE_DIR, 'db.sqlite3'),
)

SECRET_KEY = '(^%9&3b5_=1awi38u3p!$pc-0x6^(gdxkf^*_)q@%hrk_o)fa_'

# set to 'production'
env = 'local'
