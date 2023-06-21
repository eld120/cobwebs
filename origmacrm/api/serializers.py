from customer.models import Address
from rest_framework import serializers
from user.models import User


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = (
            "uuid",
            "address_1",
            "address_2",
            "city",
            "state",
            "phone",
            "email",
            "start_date",
            "end_date",
            "created_by",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
