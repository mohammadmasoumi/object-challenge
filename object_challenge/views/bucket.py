from logging import getLogger

from flask import request, make_response, jsonify
from flask.views import MethodView

from object_challenge.services import BucketService
from .mixins import AuthMixin

logger = getLogger(__name__)

__all__ = ('ArvanAPI', 'BucketAPI')

BUCKET_VALIDATORS = {
    'bucket': []
}


class BucketAPI(MethodView, AuthMixin):

    def post(self):
        response_msg = {}
        status_code = 200

        # get the post data
        post_data = request.get_json()
        user, error = self.is_authenticated(request)

        if user and not error:
            # validate required key
            validated_data = {}
            for key, validators in BUCKET_VALIDATORS.items():
                try:
                    value = post_data[key]
                    # TODO validate data
                    validated_data[key] = value
                except:  # NOQA
                    status_code = 400
                    response_msg.update({key: f"`{key}` is required!"})

            # if data is valid
            if not response_msg:
                is_allowed = BucketService(user=user).is_allowed(**validated_data)
                if is_allowed:
                    response_msg.update({"result": "ok"})
                else:
                    status_code = 400
                    response_msg.update({"result": "not allowed"})
        else:
            response_msg.update({"result": error})

        return make_response(jsonify(response_msg)), status_code


class ArvanAPI(MethodView):

    def post(self):
        """

        :return:
        """
        status_code = 200
        response_msg = {"result": "ok"}

        return make_response(jsonify(response_msg)), status_code
