import json
from logging import getLogger

from flask import request

from app import app
from object_challenge.services import BucketService

logger = getLogger(__name__)

BUCKET_VALIDATORS = {
    'username': [],
    'bucket': []
}


# @app.route('/', methods=['POST', 'GET'])
@app.route('/bucket', methods=['POST'])
def bucket_views():
    """

    :return:
    """
    request_data = request.get_json()
    response_msg = {}
    status_code = 200

    # validate
    validated_data = {}
    for key, validators in BUCKET_VALIDATORS.items():
        try:
            value = request_data[key]
            # TODO validate data
            validated_data[key] = value
        except:  # NOQA
            status_code = 400
            response_msg.update({key: f"`{key}` is required!"})

    if not response_msg:
        is_allowed = BucketService(**validated_data).is_allowed()
        if is_allowed:
            response_msg.update({"result": "ok"})
        else:
            status_code = 400
            response_msg.update({"result": "not allowed"})

    response = app.response_class(
        response=json.dumps(response_msg),
        status=status_code,
        mimetype='application/json'
    )
    return response

# @app.route('/')
# def hello_views():
#     response = app.response_class(
#         response=json.dumps({"result": "Ok"}),
#         status=200,
#         mimetype='application/json'
#     )
#     return response
