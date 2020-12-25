import mongoengine as mo


class UserPrefix(mo.Document):
    user_id = mo.IntField(null=False)
    prefix_id = mo.IntField(null=False)
    is_allowed = mo.BooleanField(default=True)

    def __str__(self):
        return f'{self.user_id}-{self.prefix_id}-{self.is_allowed}'

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
