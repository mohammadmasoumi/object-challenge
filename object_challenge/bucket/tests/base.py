from flask_mongoengine import MongoEngine
from flask_testing import TestCase

from object_challenge import app
from object_challenge.helper import load_fixture, destroy_fixture


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('object_challenge.config.TestingConfig')
        mongo_db = MongoEngine()
        mongo_db.init_app(app)
        return app

    def setUp(self):
        load_fixture(self.app)

    def tearDown(self):
        destroy_fixture(self.app)
