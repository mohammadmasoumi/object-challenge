import mongoengine as mo


class UserPrefix(mo.Document):
    user_id = mo.IntField()
    prefix_id = mo.IntField()
    is_allowed = mo.BooleanField(default=True)
