import mongoengine as mo


class Prefix(mo.Document):
    prefix_id = mo.IntField(null=False)
    prefix = mo.StringField(null=False)

    meta = {
        'index_background': True,
        'indexes': [
            'prefix_id'
        ],
        'collection': 'prefixes'
    }
