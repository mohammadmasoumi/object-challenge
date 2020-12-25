import mongoengine as mo


class User(mo.Document):
    user_id = mo.IntField(null=False, unique=True)
    name = mo.StringField(null=False)
    auth_token = mo.StringField(null=False, unique=True)

    meta = {
        'index_background': True,
        'indexes': [
            'user_id',
            'auth_token'
        ],
        'collection': 'users',
        'db_alias': 'challenge'
    }
