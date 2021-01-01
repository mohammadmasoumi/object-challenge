import os

_PREFIX = 'APP_'


def get_env_var(name, default=None, prefixed=False):
    """ Returns the value of the environment variable with th given name

    :param name: name of environment variable
    :param prefixed whether to add project name prefix to env var or not
    :param default: default value if the environment variable was not set
    :return: value of the given environment variable
    """
    key = _PREFIX + name if prefixed else name
    return os.environ.get(key, default)


PROJECT_NAME = 'object_challenge'
REDIS_HOST = get_env_var('REDIS_CACHE_HOST', 'redis', prefixed=True)
REDIS_PORT = get_env_var('REDIS_CACHE_PORT', 6379, prefixed=True)
REDIS_DB = get_env_var('REDIS_CACHE_DB', 0, prefixed=True)


class BaseConfig:
    """Base configuration."""
    DEBUG = False
    BEARER = 'Token'
    PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    REDIS_URL = f"redis://:{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True

    MONGO_DB = get_env_var('MONGO_DB', default='challenge', prefixed=True)
    MONGO_HOST = get_env_var('MONGO_HOST', default='mongo', prefixed=True)
    MONGO_PORT = int(get_env_var('MONGO_PORT', default=27017, prefixed=True))
    MONGO_USERNAME = get_env_var('MONGO_USERNAME', default='challenge', prefixed=True)
    MONGO_PASSWORD = get_env_var('MONGO_PASSWORD', default='challenge', prefixed=True)

    MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
    MONGODB_SETTINGS = {
        'db': MONGO_DB,
        'host': MONGO_HOST,
        'port': MONGO_PORT,
        'username': MONGO_USERNAME,
        'password': MONGO_PASSWORD,
        'connect': False,
        'alias': 'challenge'
    }
    REDIS_SETTINGS = {
        'db': get_env_var('REDIS_CACHE_DB', 10, prefixed=True),
        'host': REDIS_HOST,
        'port': REDIS_PORT
    }


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True

    MONGO_DB = get_env_var('MONGO_DB', default='test', prefixed=True)
    MONGO_HOST = get_env_var('MONGO_HOST', default='mongo', prefixed=True)
    MONGO_PORT = int(get_env_var('MONGO_PORT', default=27017, prefixed=True))
    MONGO_USERNAME = get_env_var('MONGO_USERNAME', default='test', prefixed=True)
    MONGO_PASSWORD = get_env_var('MONGO_PASSWORD', default='test', prefixed=True)

    MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
    MONGODB_SETTINGS = {
        'db': MONGO_DB,
        'host': MONGO_HOST,
        'port': MONGO_PORT,
        'username': MONGO_USERNAME,
        'password': MONGO_PASSWORD,
        'connect': False,
        'alias': 'test'
    }
    REDIS_SETTINGS = {
        'db': get_env_var('REDIS_CACHE_DB', 10, prefixed=True),
        'host': REDIS_HOST,
        'port': REDIS_PORT
    }


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = get_env_var("SECRET_KEY", default=os.urandom(64))
    DEBUG = False

    MONGO_DB = get_env_var('MONGO_DB', default='challenge', prefixed=True)
    MONGO_HOST = get_env_var('MONGO_HOST', default='mongo', prefixed=True)
    MONGO_PORT = int(get_env_var('MONGO_PORT', default=27017, prefixed=True))
    MONGO_USERNAME = get_env_var('MONGO_USERNAME', default='challenge', prefixed=True)
    MONGO_PASSWORD = get_env_var('MONGO_PASSWORD', default='challenge', prefixed=True)

    MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
    MONGODB_SETTINGS = {
        'db': MONGO_DB,
        'host': MONGO_HOST,
        'port': MONGO_PORT,
        'username': MONGO_USERNAME,
        'password': MONGO_PASSWORD,
        'connect': False,
        'alias': 'challenge'
    }
    REDIS_SETTINGS = {
        'db': get_env_var('REDIS_CACHE_DB', 10, prefixed=True),
        'host': REDIS_HOST,
        'port': REDIS_PORT
    }
