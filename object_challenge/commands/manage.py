import os

import click
import ujson
from flask.cli import AppGroup

from object_challenge.mongo_models import User

__all__ = ('management_cli',)

management_cli = AppGroup('manage')


@management_cli.command('initial')
def init_data():
    from app import app

    click.echo("Initializing data")

    path = os.path.join(app.config['PROJECT_ROOT'], 'object_challenge', 'fixtures')
    filenames = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for filename in filenames:
        col_name = filename[:-5]
        with open(os.path.join(path, filename)) as file:
            for row in file.readlines():
                User._get_db()[col_name].insert_one(ujson.loads(row))

    click.echo("Initializing data has been finished successfully!")
