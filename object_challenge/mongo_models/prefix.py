import mongoengine as mo


class Prefix(mo.Document):
    prefix_id = mo.IntField(null=False, unique=True)
    prefix = mo.StringField(null=False, unique=True)

    meta = {
        'index_background': True,
        'indexes': [
            'prefix_id'
        ],
        'collection': 'prefixes',
        'db_alias': 'challenge'
    }
