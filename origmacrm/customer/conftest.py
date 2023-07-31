import pytest
from user.conftest import user_one
from user.factories import UserFactory

from .factories import AddressFactory, CustomerFactory


@pytest.fixture
def address_one():
    return AddressFactory(created_by=UserFactory(password="password123"))


@pytest.fixture
def customer_one(rando_user, address_one):
    return CustomerFactory(created_by=rando_user, billing_address=address_one)


@pytest.fixture
def customer_two():
    return CustomerFactory(
        created_by=user_one,
        billing_address=AddressFactory(address_1="123 Fake St", created_by=user_one),
        shipping_addresses=AddressFactory(
            address_1="456 Flaming Lava Cir", created_by=user_one
        ),
    )
