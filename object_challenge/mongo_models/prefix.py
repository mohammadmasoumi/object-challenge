import mongoengine as mo


class Prefix(mo.Document):
    pk = mo.IntField(null=False)
    prefix = mo.StringField(null=False)

    meta = {
        'index_background': True,
        'indexes': [
            'pk'
        ],
        'collection': 'prefixes'
    }
