import os

from flask import Flask
from flask_mongoengine import MongoEngine

PROJECT_ENV = os.environ.get('ENV', 'development')

app = Flask(__name__)
app.config.update({'ENV': PROJECT_ENV})
app.config.from_object(f'settings.{PROJECT_ENV}')

# import views
from views import *  # NOQA

# mongo db configuration
db = MongoEngine()
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
