from base import venv

MONGO_CONFIG = {
    'db': venv.get_env_var('MONGO_DB', default='my_db', prefixed=True),
    'host': venv.get_env_var('MONGO_HOST', default='localhost', prefixed=True),
    'port': venv.get_env_var('MONGO_PORT', default=27017, prefixed=True),
}
