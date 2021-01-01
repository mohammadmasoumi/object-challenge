import os
import unittest

import coverage
from flask_script import Manager

COV = coverage.coverage(
    branch=True,
    include='object_challenge/*',
    omit=[
        'object_challenge/tests/*',
        'object_challenge/config.py',
        'object_challenge/*/__init__.py'
    ]
)
COV.start()

# register app
from object_challenge import app, mongoengine, pymongo, redis_store  # NOQA
from object_challenge.helper import load_fixture  # NOQA

mongoengine.init_app(app)
pymongo.init_app(app)
redis_store.init_app(app)

manager = Manager(app)


@manager.command
def init():
    load_fixture()


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('object_challenge/bucket/', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('object_challenge/bucket/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
