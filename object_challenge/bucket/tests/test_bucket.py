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


def create_arvan(self, bucket, token):
    return self.client.post(
        '/arvan',
        data=json.dumps(dict(
            bucket=bucket,
        )),
        headers=dict(Authorization=f'{self.app.config["BEARER"]} {token}'),
        content_type='application/json',
    )


class TestBucketAPI(BaseTestCase):

    def test_create_bucket(self):
        """
        test create not assigned bucket
        """
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

    def test_create_allowed_bucket(self):
        """
        test create allowed bucket
        """
        with self.client:
            data = {
                'bucket': 'arvan3',
                'token': 'token_1'
            }
            response = create_bucket(self, **data)
            data = json.loads(response.data.decode())

            self.assertEqual(data.get('result'), 'ok')
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_create_not_allowed_bucket(self):
        """
        test create not allowed bucket
        """
        with self.client:
            data = {
                'bucket': 'pushe3',
                'token': 'token_1'
            }
            response = create_bucket(self, **data)
            data = json.loads(response.data.decode())

            self.assertEqual(data.get('result'), 'not allowed')
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 400)


class TestArvanAPI(BaseTestCase):

    def test_create_arvan(self):
        """
        test create validated bucket in arvan
        """
        with self.client:
            data = {
                'bucket': 'test',
                'token': 'token_1'
            }
            response = create_arvan(self, **data)
            data = json.loads(response.data.decode())

            self.assertEqual(data.get('result'), 'ok')
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
