import mongoengine as mo


class Prefix(mo.Document):
    prefix_id = mo.IntField(null=False, unique=True)
    prefix = mo.StringField(null=False, unique=True)

    def __str__(self):
        return f"{self.prefix_id}, {self.prefix}"

    meta = {
        'index_background': True,
        'collection': 'prefixes',
        'indexes': [
            'prefix_id'
        ]
    }
