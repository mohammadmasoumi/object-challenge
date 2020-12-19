import logging
import os

from flask import Flask
from flask_mongoengine import MongoEngine

PROJECT_ENV = os.environ.get('ENV', 'development')

app = Flask(__name__)
app.config.from_object(f'settings.{PROJECT_ENV}')

# import views
from views import *  # NOQA

# mongo db configuration
db = MongoEngine()
db.init_app(app)

# logging configuration
handler = logging.StreamHandler()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(module)s.%(name)s.%(funcName)s | %(msg)s',
)

if __name__ == '__main__':
    app.run(debug=True)
