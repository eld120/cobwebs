import pytest

from .factories import UserFactory


@pytest.fixture
def rando_user():
    return UserFactory()


@pytest.fixture
def user_one():
    return UserFactory(name="Willy Wonka")
