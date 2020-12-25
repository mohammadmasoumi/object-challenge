import re

from object_challenge import pymongo

__all__ = ('BucketService',)


class BucketService:

    def __init__(self, user):
        """
        constructor
        :param user: user
        """
        assert user, "`user` is required"
        self.user = user

    def is_allowed(self, **data):
        """
        indicates whether user can create specified bucket or not
        :param data: bucket data
        :return: bool
        """
        assert data.get('bucket'), "`bucket` is required"

        # indicates whether user is allowed or not
        is_allowed = True

        # buckets at least should have 3 characters
        # we get 2 first characters for database lookup
        bucket = data['bucket'][:2].lower()

        # Note also that regex's anchored at the start (ie: starting with ^) are able to use indexes in the db,
        # and will run much faster in that case.
        r_bucket = re.compile(f'^{bucket}', re.IGNORECASE)

        # user can create new bucket under 3 circumstances:
        #   1. prefix doesn't exists in the db
        #   2. the prefix was assigned to the user
        #   3. the prefix wasn't forbidden for this user
        user_prefixes = tuple(pymongo.db.prefixes.aggregate([
            {'$match': {'prefix': {'$regex': r_bucket}}},
            {'$lookup': {
                'from': 'user_prefixes',
                'localField': 'prefix_id',
                'foreignField': 'prefix_id',
                'as': 'user_prefixes'
            }},
            {'$unwind': '$user_prefixes'},
            {'$match': {'$or': [
                {'user_id': {'$ne': self.user.user_id}},
                {'user_id': self.user.user_id, 'is_allowed': False}
            ]}}
        ]))

        if user_prefixes:
            for item in user_prefixes:
                if bucket.startswith(item['prefix']):
                    is_allowed = False
                    break

        return is_allowed
