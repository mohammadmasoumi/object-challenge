import logging
import os

from flask import Flask
from flask_mongoengine import MongoEngine
from redis import Redis

# before app initialization
PROJECT_NAME = 'object_challenge'
APP_ENV = os.environ.get('ENV', 'development')
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.join(PROJECT_ROOT, PROJECT_NAME)

# app
app = Flask(__name__)
app.config.update({'ENV': APP_ENV})
app.config.update({'PROJECT_ROOT': PROJECT_ROOT})
app.config.update({'PROJECT_PATH': PROJECT_PATH})
app.config.from_object(f'{PROJECT_NAME}.settings.{APP_ENV}')

# mongo db configuration
db = MongoEngine()
db.init_app(app)

# # redis configuration
redis = Redis(**app.config['REDIS_SETTINGS'])

from object_challenge.commands import *  # NOQA

if __name__ == '__main__':
    app.run(debug=True)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
