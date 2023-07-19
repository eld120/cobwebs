# import pytest
import customer.views as views
import pytest
from django.test import Client, RequestFactory, TestCase
from user.factories import UserFactory

from ..conftest import address_one, customer_one, customer_two


class CustomerTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory(password="lolz_password123")
        self.customer_one = customer_one
        self.customer_two = customer_two
        self.client = Client()
        self.rf = RequestFactory()

    def tearDown(self):
        del self.user
        del self.customer_one
        del self.customer_two
        del self.client
        del self.rf

    def test_homepage(self):
        # duplicate code
        request = self.rf.get("/")
        response = views.HomePage.as_view()(request)
        assert response.status_code == 200
        assert response.template_name[0] == "index.html"

        login = self.client.login(
            username=self.user.username, password="lolz_password123"
        )
        assert login

        response = self.client.get("/")
        assert response.status_code == 200
        assert response.template_name[0] == "index.html"

    # def test_customer_detailview(self):
    #     request = self.rf.get(f'customer/{self.customer_one.uuid}' )
    #     response = views.CustomerDetailView.as_view()(request)
    #     assert response.status_code == 200
    #     assert response.template_name[0] == "customer/customer_detail.html"


class AddressTestCase(TestCase):
    def setUp(self):
        self.address = address_one
        self.client = Client()
        self.customer_one = customer_one
        self.customer_two = customer_two

    def tearDown(self):
        del self.address
        del self.client
        del self.customer_one
        del self.customer_two


@pytest.mark.django_db
def test_customer_detailview(rf, client, customer_one):
    user = UserFactory(password="sUpErSecrEtwOrdS")
    response = client.login(username=user.username, password="sUpErSecrEtwOrdS")
    assert response
    request = rf.get(f"/customer/{customer_one.uuid}")
    request.user = user
    response = views.CustomerDetailView.as_view()(request, uuid=customer_one.uuid)
    assert response.status_code == 200
    assert response.template_name[0] == "customer/customer_detail.html"
