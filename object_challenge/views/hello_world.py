from logging import getLogger

from app import app
from object_challenge.mongo_models import User

logger = getLogger(__name__)


@app.route('/')
def hello_world():
    print(User.objects.filter())
    return 'Hello World!'


