import mongoengine as mo


class UserPrefix(mo.Document):
    user_pk = mo.IntField(null=False)
    prefix_pk = mo.IntField(null=False)
    is_allowed = mo.BooleanField(default=True)

    meta = {
        'index_background': True,
        'collection': 'user_prefixes',
        'indexes': [
            {
                'fields': [
                    'user_pk', 'prefix_pk', 'is_allowed'
                ]
            },
        ],
    }
