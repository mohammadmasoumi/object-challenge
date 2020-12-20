import os

from flask import Flask
from flask_mongoengine import MongoEngine

# before app initialization
PROJECT_NAME = 'object_challenge'
APP_ENV = os.environ.get('ENV', 'development')
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.join(PROJECT_ROOT, PROJECT_NAME)

# app
application = Flask(__name__)
application.config.update({'ENV': APP_ENV})
application.config.from_object(f'{PROJECT_NAME}.settings.{APP_ENV}.py')

# import views
from object_challenge.views import *  # NOQA

# mongo db configuration
db = MongoEngine()
db.init_app(application)

if __name__ == '__main__':
    application.logger.info("********************* CONFIG *********************")
    for key, value in application.config.items():
        application.logger.info(f"{key}: {value}")
    application.logger.info("**************************************************")

    application.run(debug=True)
