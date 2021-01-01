import os

from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from flask_redis import FlaskRedis
from mockredis import MockRedis

app = Flask(__name__)
CORS(app)

app_settings = os.environ.get(
    'ENV',
    'object_challenge.config.DevelopmentConfig'
)

app = Flask(__name__)
app.config.from_object(app_settings)

# mongo configuration
mongoengine = MongoEngine()
pymongo = PyMongo()

if app.testing:
    redis_store = FlaskRedis.from_custom_provider(MockRedis)
else:
    redis_store = FlaskRedis()

from object_challenge.bucket.views import bucket_blueprint  # NOQA

app.register_blueprint(bucket_blueprint)
