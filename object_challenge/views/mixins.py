from object_challenge.base import User
from object_challenge.mongo_models import User as UserDocument


class AuthMixin:
    _BEARER = 'Bearer'
    DEFAULT_AUTH_ERRORS = {
        'bearer': "Invalid authorization `bearer`",
        'token': "Invalid user `token`"
    }

    def _fetch_user(self, token):
        """

        :param token:
        :return:
        """
        user_data = UserDocument._get_collection().find_one({'token': token})
        if user_data:
            return User(**user_data)

    def is_authenticated(self, request):
        """

        :param request:
        :return:
        """
        user = None
        error = None

        auth_header = request.headers.get('Authorization')
        if auth_header:
            bearer, token = auth_header.split(' ')
            if bearer == self._BEARER:
                if token:
                    user = self._fetch_user(token)
                    if not user:
                        error = self.DEFAULT_AUTH_ERRORS['token']
                else:
                    error = self.DEFAULT_AUTH_ERRORS['token']
            else:
                error = self.DEFAULT_AUTH_ERRORS['bearer']

        return user, error
