import os

from object_challenge.base import venv

MONGODB_SETTINGS = {
    'db': venv.get_env_var('MONGO_DB', default='challenge', prefixed=True),
    'host': venv.get_env_var('MONGO_HOST', default='mongo', prefixed=True),
    'port': int(venv.get_env_var('MONGO_PORT', default=27017, prefixed=True)),
    'username': venv.get_env_var('MONGO_USERNAME', default='challenge', prefixed=True),
    'password': venv.get_env_var('MONGO_PASSWORD', default='challenge', prefixed=True),
    'connect': False
}

SECRET_KEY = venv.get_env_var("SECRET_KEY", default=os.urandom(64))
