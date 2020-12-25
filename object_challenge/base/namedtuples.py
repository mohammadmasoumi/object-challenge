from collections import namedtuple

__all__ = ('UserObj',)


class UserObj(namedtuple('UserObj', ('user_id', 'name', 'auth_token'))):
    pass
