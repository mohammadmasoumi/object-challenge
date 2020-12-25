# project/tests/base.py


from flask_testing import TestCase

from object_challenge import app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('object_challenge.config.TestingConfig')
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass
