import os

from object_challenge.base import utilities

MONGODB_SETTINGS = {
    'db': utilities.get_env_var('MONGO_DB', default='challenge', prefixed=True),
    'host': utilities.get_env_var('MONGO_HOST', default='mongo', prefixed=True),
    'port': int(utilities.get_env_var('MONGO_PORT', default=27017, prefixed=True)),
    'username': utilities.get_env_var('MONGO_USERNAME', default='challenge', prefixed=True),
    'password': utilities.get_env_var('MONGO_PASSWORD', default='challenge', prefixed=True),
    'connect': False
}

SECRET_KEY = utilities.get_env_var("SECRET_KEY", default=os.urandom(64))
