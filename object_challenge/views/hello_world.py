import json
from logging import getLogger

from app import app
from object_challenge.mongo_models import User

logger = getLogger(__name__)


@app.route('/')
def hello_world():
    app.logger.info(f"users: {User.objects.filter()}")
    User.objects.create(user_id=1, name='asghar')
    app.logger.info("-------------------------------")
    response = app.response_class(
        response=json.dumps({"result": "OK"}),
        status=200,
        mimetype='application/json'
    )
    return response
