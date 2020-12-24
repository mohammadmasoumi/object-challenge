from app import app
from object_challenge.mongo_models import UserPrefix

__all__ = ('BucketService',)


class BucketService:

    def __init__(self, user_id, bucket):
        self.user_id = user_id
        self.bucket = bucket

    def is_allowed(self):
        user_prefixes = tuple(UserPrefix._get_collection().aggregate([
            {'$match': {'user_id': self.user_id}},
            {'$lookup': {
                'from': 'prefixes',
                'localField': 'prefix_id',
                'foreignField': 'prefix_id',
                'as': 'user_prefixes',
            }},
            {'$project': {'$user_prefixes': 1, '$is_allowed': 1, '_id': 0}}
        ]))

        for item in user_prefixes:
            app.logger.info(f"item: {item}")

        return True
