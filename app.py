from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_mongoengine import MongoEngine

from settings import development as settings  # TODO read settings from env

app = Flask(__name__)

# mongo db configuration
app.config['MONGODB_SETTINGS'] = settings.MONGO_CONFIG
db = MongoEngine()
db.init_app(app)

# debug mode configuration
app.config['DEBUG_TB_PANELS'] = ['flask_mongoengine.panels.MongoDebugPanel']
toolbar = DebugToolbarExtension(app)

if __name__ == '__main__':
    app.run()
