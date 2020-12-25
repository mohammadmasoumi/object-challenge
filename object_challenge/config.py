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


class BaseConfig:
    """Base configuration."""
    DEBUG = False
    PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': get_env_var('MONGO_DB', default='challenge', prefixed=True),
        'host': get_env_var('MONGO_HOST', default='mongo', prefixed=True),
        'port': int(get_env_var('MONGO_PORT', default=27017, prefixed=True)),
        'username': get_env_var('MONGO_USERNAME', default='challenge', prefixed=True),
        'password': get_env_var('MONGO_PASSWORD', default='challenge', prefixed=True),
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
    MONGODB_SETTINGS = {
        'db': get_env_var('MONGO_DB', default='challenge', prefixed=True),
        'host': get_env_var('MONGO_HOST', default='mongo', prefixed=True),
        'port': int(get_env_var('MONGO_PORT', default=27017, prefixed=True)),
        'username': get_env_var('MONGO_USERNAME', default='challenge', prefixed=True),
        'password': get_env_var('MONGO_PASSWORD', default='challenge', prefixed=True),
        'connect': False,
        'alias': 'challenge'
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
    MONGODB_SETTINGS = {
        'db': get_env_var('MONGO_DB', default='challenge', prefixed=True),
        'host': get_env_var('MONGO_HOST', default='mongo', prefixed=True),
        'port': int(get_env_var('MONGO_PORT', default=27017, prefixed=True)),
        'username': get_env_var('MONGO_USERNAME', default='challenge', prefixed=True),
        'password': get_env_var('MONGO_PASSWORD', default='challenge', prefixed=True),
        'connect': False,
        'alias': 'challenge'
    }
    REDIS_SETTINGS = {
        'db': get_env_var('REDIS_CACHE_DB', 10, prefixed=True),
        'host': REDIS_HOST,
        'port': REDIS_PORT
    }
