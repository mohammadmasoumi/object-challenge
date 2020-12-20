from logging import getLogger

from app import application
from object_challenge.mongo_models import User

logger = getLogger(__name__)


@application.route('/')
def hello_world():
    print(User.objects.filter())
    return 'Hello World!'
