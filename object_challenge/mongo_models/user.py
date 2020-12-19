import mongoengine as mo


class User(mo.Document):
    user_id = mo.IntField(null=False)
    name = mo.StringField(null=False)

    meta = {
        'index_background': True,
        'indexes': [
            'user_id'
        ],
        'collection': 'users'
    }
