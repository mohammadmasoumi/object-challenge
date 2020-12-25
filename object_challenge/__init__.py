import os

from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine

app = Flask(__name__)
CORS(app)

app_settings = os.environ.get(
    'ENV',
    'object_challenge.config.DevelopmentConfig'
)

app = Flask(__name__)
app.config.from_object(app_settings)

# mongo configuration
mongo_db = MongoEngine()

from object_challenge.bucket.views import bucket_blueprint  # NOQA

app.register_blueprint(bucket_blueprint)
