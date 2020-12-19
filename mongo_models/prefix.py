import mongoengine as mo


class Prefix(mo.Document):
    id = mo.IntField()
    prefix = mo.StringField()
