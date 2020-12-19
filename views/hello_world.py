from logging import getLogger

from app import app
from mongo_models import User

logger = getLogger(__name__)


@app.route('/')
def hello_world():
    logger.info("-----------------------------------")
    logger.info(app.config)
    logger.info("-----------------------------------")

    print(User.objects.filter())
    return 'Hello World!'
