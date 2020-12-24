from app import db

__all__ = ('BucketService',)


class BucketService:

    def __init__(self, username, bucket):
        self.username = username
        self.bucket = bucket

    def is_allowed(self):
        db['user_prefixes'].aggregate([
            {'$lookup': {
                'from': None,
                'localField': None,
                'foreignField': None,
                'as': None
            }}
        ])

        return True
