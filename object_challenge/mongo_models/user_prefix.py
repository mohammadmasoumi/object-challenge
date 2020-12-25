import mongoengine as mo


class UserPrefix(mo.Document):
    user_id = mo.IntField(null=False)
    prefix_id = mo.IntField(null=False)
    is_allowed = mo.BooleanField(default=True)

    meta = {
        'index_background': True,
        'collection': 'user_prefixes',
        'indexes': [
            {
                'fields': [
                    'user_id', 'prefix_id', 'is_allowed'
                ]
            },
        ],
        'db_alias': 'challenge'
    }
