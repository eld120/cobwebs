import factory
from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda x: f"rando_bot_{x}")
    name = factory.Faker("name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "password")

    class Meta:
        model = get_user_model()
