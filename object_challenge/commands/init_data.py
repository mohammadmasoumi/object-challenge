import os
from app import app
from object_challenge.base import DataLoaderMixin


@app.cli.command('init-data')
def init_data():
    path = os.path.join(app.config['PROJECT_ROOT'], 'object_challenge', 'fixtures')
    filenames = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for filename in filenames:
        DataLoaderMixin.load_data(filename)
