import os
import unittest

import coverage
import ujson
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
from object_challenge import app, mongo_db  # NOQA

mongo_db.init_app(app)

manager = Manager(app)


@manager.command
def init():
    from object_challenge.bucket.mongo_models import User
    path = os.path.join(app.config['PROJECT_DIR'], 'bucket', 'fixtures')
    filenames = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for filename in filenames:
        col_name = filename[:-5]
        with open(os.path.join(path, filename)) as file:
            for row in file.readlines():
                User._get_db()[col_name].insert_one(ujson.loads(row))


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
