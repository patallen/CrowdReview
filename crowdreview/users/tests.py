from django.test import TestCase


class UserTests(TestCase):
    def test_signup_page_status_ok(self):
        res = self.client.get('/users/signup/')
        self.assertEqual(res.status_code, 200)

    def test_signup_page_template(self):
        res = self.client.get('/users/signup/')
        self.assertIn('<html>', str(res.content))
