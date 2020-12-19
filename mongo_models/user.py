import mongoengine as mo


class User(mo.Document):
    id = mo.IntField()
    name = mo.StringField()
