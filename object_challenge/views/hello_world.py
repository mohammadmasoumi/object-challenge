import json
from logging import getLogger

from app import app
from object_challenge.mongo_models import User

logger = getLogger(__name__)


@app.route('/')
def hello_world():
    print(User.objects.filter())

    response = app.response_class(
        response=json.dumps({"result": "OK"}),
        status=200,
        mimetype='application/json'
    )
    return response
