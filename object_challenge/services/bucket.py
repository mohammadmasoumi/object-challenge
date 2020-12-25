import re

from app import app
from object_challenge.mongo_models import Prefix

__all__ = ('BucketService',)


class BucketService:

    def __init__(self, user):
        """

        :param user:
        """
        assert user, "`user` is required"
        self.user = user

    def is_allowed(self, data):
        """

        :param data:
        :return:
        """
        assert data.get('bucket'), "`bucket` is required"

        # buckets at least should have 3 characters
        # we get 2 first characters for database lookup
        bucket = data['bucket'][:2].lower()

        # Note also that regex's anchored at the start (ie: starting with ^) are able to use indexes in the db,
        # and will run much faster in that case.
        r_bucket = re.compile(f'^{bucket}', re.IGNORECASE)

        user_prefixes = tuple(Prefix._get_collection().aggregate([
            {'$match': {'prefix': {'$regex': r_bucket}}},
            {'$lookup': {
                'from': 'user_prefixes',
                'localField': 'prefix_id',
                'foreignField': 'prefix_id',
                'as': 'user_prefixes',
            }}
        ]))

        for item in user_prefixes:
            app.logger.info(f"item: {item}")

        return True
