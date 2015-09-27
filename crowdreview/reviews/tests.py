from django.test import TestCase

# Create your tests here.

class PublicTests(TestCase):
    def test_homepage_status_ok(self):
        res = self.client.get('/')
        print(res)
        self.assertEqual(res.status_code, 200)
