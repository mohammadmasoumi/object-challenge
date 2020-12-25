from logging import getLogger

from flask import Blueprint
from flask import request, make_response, jsonify
from flask.views import MethodView

from object_challenge.bucket.services import BucketService
from object_challenge.base.mixins import AuthMixin

logger = getLogger(__name__)

__all__ = ('bucket_blueprint',)

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


# define blueprint
bucket_blueprint = Blueprint('bucket', __name__)

# add Rules for API Endpoints and the API resources
bucket_blueprint.add_url_rule(
    '/bucket',
    view_func=BucketAPI.as_view('bucket_api'),
    methods=['POST']
)

bucket_blueprint.add_url_rule(
    '/arvan',
    view_func=ArvanAPI.as_view('arvan_api'),
    methods=['POST']
)
