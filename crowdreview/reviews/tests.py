from django.test import TestCase


class PublicTests(TestCase):
    def test_homepage_status_ok(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
