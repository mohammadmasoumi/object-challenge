import json
import unittest

from object_challenge.bucket.tests.base import BaseTestCase


def create_bucket(self, bucket, token):
    return self.client.post(
        '/bucket',
        data=json.dumps(dict(
            bucket=bucket,
        )),
        headers=dict(Authorization=f'{self.app.config["BEARER"]} {token}'),
        content_type='application/json',
    )


class TestAuthBlueprint(BaseTestCase):

    def test_create_bucket(self):
        """ Test for bucket creation"""
        with self.client:
            data = {
                'bucket': 'test',
                'token': 'token_1'
            }
            response = create_bucket(self, **data)
            data = json.loads(response.data.decode())

            self.assertEqual(data.get('result'), 'ok')
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
