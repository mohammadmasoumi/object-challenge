import mongoengine as mo


class Prefix(mo.Document):
    id = mo.IntField()
    prefix = mo.StringField()

    meta = {
        'index_background': True,
        'indexes': [
            'id'
        ],
        'collection': 'prefixes'
    }
