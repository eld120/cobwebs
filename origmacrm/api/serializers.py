from customer.models import Address
from rest_framework import serializers
from user.models import User


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = (
            "dba",
            "name",
            "billing_address",
            "shipping_address",
            "start_date",
            "end_date",
            "active",
            "customer_type",
        )


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = (
            "address_1",
            "address_2",
            "city",
            "state",
            "phone",
            "email",
            "start_date",
            "end_date",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
