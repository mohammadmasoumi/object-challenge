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

app.logger.info("-----------------------------------")
print(f"PROJECT_ENV: {PROJECT_ENV}")
for key, value in app.config.items():
    app.logger.info(f"-- {key}: {value}")
app.logger.info("-----------------------------------")

if __name__ == '__main__':
    app.run(debug=True)
