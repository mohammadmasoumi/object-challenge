import mongoengine as mo


class User(mo.Document):
    pk = mo.IntField(null=False)
    name = mo.StringField(null=False)

    meta = {
        'index_background': True,
        'indexes': [
            'pk'
        ],
        'collection': 'users'
    }
