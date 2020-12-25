from flask import Blueprint

from app import app
from .bucket import BucketAPI, ArvanAPI

# define the API resources
bucket_view = BucketAPI.as_view('bucket_api')
arvan_view = ArvanAPI.as_view('arvan_api')

bucket_blueprint = Blueprint('bucket', f'{__name__}.bucket')

# add Rules for API Endpoints
bucket_blueprint.add_url_rule(
    '/bucket',
    view_func=bucket_view,
    methods=['POST']
)

bucket_blueprint.add_url_rule(
    '/arvan',
    view_func=arvan_view,
    methods=['POST']
)

# register views
app.register_blueprint(bucket_blueprint)
