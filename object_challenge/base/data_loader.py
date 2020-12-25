import os
import ujson
from app import db, PROJECT_ROOT

__all__ = ('DataLoaderMixin',)


class DataLoaderMixin:

    @staticmethod
    def load_data(filename):
        path = os.path.join(PROJECT_ROOT, 'object_challenge', 'fixtures', filename)
        col_name = filename[:-5]

        with open(path) as file:
            for row in file.readlines():
                db[col_name].insert_one(ujson.loads(row))
