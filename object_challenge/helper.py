import os

import ujson


def load_fixture():
    from object_challenge import app, pymongo
    app.logger.info("Start loading fixtures ...")

    path = os.path.join(app.config['PROJECT_DIR'], 'bucket', 'fixtures')
    filenames = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for filename in filenames:
        col_name = filename[:-5]
        with open(os.path.join(path, filename)) as file:
            for row in file.readlines():
                pymongo.db[col_name].insert_one(ujson.loads(row))

    app.logger.info("loading fixtures have been finished successfully!")


def destroy_fixture():
    from object_challenge import app, pymongo

    app.logger.info("Start dropping collections ...")

    path = os.path.join(app.config['PROJECT_DIR'], 'bucket', 'fixtures')
    filenames = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for filename in filenames:
        col_name = filename[:-5]
        pymongo.db.drop_collection(col_name)

    app.logger.info("Dropping all collections have been finished successfully!")
