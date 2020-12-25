from collections import namedtuple


class User(namedtuple('User', ('user_id', 'name', 'token'))):
    pass
