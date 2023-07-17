import datetime

import factory
from user.factories import UserFactory

from .models import ACTIVE_OPTIONS, Customer


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "customer.Address"

    start_date = factory.Faker(
        "date_between_dates",
        date_start=datetime.date(2020, 1, 1),
        date_end=datetime.date(2024, 5, 31),
    )
    end_date = None
    created_by = factory.SubFactory(UserFactory)
    address_1 = factory.faker("street_address")
    address_2 = factory.faker()
    city = factory.faker("city")
    state = factory.faker("state")
    zip_code = factory.faker("postcode")
    phone = factory.faker("basic_phone_number")
    email = factory.faker("ascii_free_email")


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "customer.Customer"

    start_date = factory.Faker(
        "date_between_dates",
        date_start=datetime.date(2020, 1, 1),
        date_end=datetime.date(2024, 5, 31),
    )
    end_date = None
    created_by = factory.SubFactory(UserFactory)
    dba = factory.Faker("text", max_nb_chars=20)
    name = factory.Faker("text", max_nb_chars=20)
    billing_address = factory.SubFactory(AddressFactory)
    shipping_address = factory.SubFactory(AddressFactory)
    active = factory.Faker(
        "random_element", element=[choice[1] for choice in ACTIVE_OPTIONS]
    )
    customer_type = factory.Faker(
        "random_element", element=[choice[1] for choice in Customer.INDUSTRY_OPTIONS]
    )
