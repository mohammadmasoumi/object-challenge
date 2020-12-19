from app import app
from mongo_models import User


@app.route('/')
def hello_world():
    print(User.objects.filter())
    return 'Hello World!'
