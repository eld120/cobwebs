import pytest

from .factories import UserFactory


@pytest.fixture
def rando_user():
    return UserFactory(password="sUpErSecrEtwOrdS")


@pytest.fixture
def user_one():
    return UserFactory(password="lolz_password123")
