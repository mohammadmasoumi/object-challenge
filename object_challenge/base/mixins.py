from object_challenge import app
from object_challenge.base import UserObj
from object_challenge.bucket.mongo_models import User as UserDocument


class AuthMixin:
    _BEARER = 'Token'
    DEFAULT_AUTH_ERRORS = {
        'bearer': "Invalid authorization `bearer`",
        'token': "Invalid user `token`"
    }

    def _fetch_user(self, token):
        """

        :param token:
        :return:
        """
        user_data = UserDocument._get_collection().find_one({'auth_token': token}, {'_id': 0})
        if user_data:
            return UserObj(**user_data)

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
            app.logger.info(f"token: {token} | bearer: {bearer}")
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
