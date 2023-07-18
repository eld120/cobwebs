from django.test import Client, TestCase


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login(self):
        response = self.client.get("user/login/")
        assert response.status_code == 200
