import logging
import os

from flask import Flask
from flask_mongoengine import MongoEngine

# before app initialization
PROJECT_NAME = 'object_challenge'
APP_ENV = os.environ.get('ENV', 'development')
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.join(PROJECT_ROOT, PROJECT_NAME)

# app
app = Flask(__name__)
app.config.update({'ENV': APP_ENV})
app.config.from_object(f'{PROJECT_NAME}.settings.{APP_ENV}')


@app.route('/')
def hello_views():
    response = app.response_class(
        response=json.dumps({"result": "Ok"}),
        status=200,
        mimetype='application/json'
    )
    return response


# import views
from object_challenge.views import *  # NOQA

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

# mongo db configuration
db = MongoEngine()
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
