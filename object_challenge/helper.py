import os

import ujson


def load_fixture(current_app):
    from object_challenge.bucket.mongo_models import User
    current_app.logger.info("Start loading fixtures ...")

    path = os.path.join(current_app.config['PROJECT_DIR'], 'bucket', 'fixtures')
    filenames = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for filename in filenames:
        col_name = filename[:-5]
        with open(os.path.join(path, filename)) as file:
            for row in file.readlines():
                User._get_db()[col_name].insert_one(ujson.loads(row))

    current_app.logger.info("loading fixtures have been finished successfully!")


def destroy_fixture(current_app):
    from object_challenge.bucket.mongo_models import User
    current_app.logger.info("Start dropping collections ...")

    path = os.path.join(current_app.config['PROJECT_DIR'], 'bucket', 'fixtures')
    filenames = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for filename in filenames:
        col_name = filename[:-5]
        User._get_db().drop_collection(col_name)

    current_app.logger.info("Dropping all collections have been finished successfully!")
