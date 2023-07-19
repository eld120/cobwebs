from customer.views import CustomerListView
from django.test import Client, RequestFactory, TestCase

from ..factories import UserFactory
from ..views import UserLoginView


class UserTestCase(TestCase):
    # are all of these requests or responses idk

    def setUp(self):
        self.rf = RequestFactory()
        self.user = UserFactory(password="testpassword")
        self.client = Client()

    def tearDown(self):
        del self.user

    def test_home_page(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert response.template_name[0] == "index.html"

    def test_dashboard(self):
        request = self.rf.get("/dashboard/")
        response = CustomerListView.as_view()(request)
        assert response.status_code == 302

        unauthorized_response = self.client.get("/dashboard/")
        assert unauthorized_response.status_code == 302
        login = self.client.login(username=self.user.username, password="testpassword")
        assert login
        response = self.client.get("/dashboard/")
        assert response.status_code == 200
        assert response.template_name[0] == "dashboard.html"

    def test_login(self):
        request = self.rf.get("/user/login/")
        response = UserLoginView.as_view()(request)
        response.status_code == 200
        response.template_name[0] == "user/login.html"
        response = self.client.post(
            "/user/login", {"username": self.user.username, "password": "testpassword"}
        )
        assert response.status_code == 200
