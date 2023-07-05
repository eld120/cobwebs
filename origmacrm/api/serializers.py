from customer.models import Address, Customer
from rest_framework import serializers
from user.models import User


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    billing_address = serializers.HyperlinkedRelatedField(
        view_name="api:address-detail",
        lookup_field="uuid",
        many=False,
        queryset=Customer.objects.all(),
    )
    shipping_address = serializers.HyperlinkedRelatedField(
        view_name="api:address-detail",
        lookup_field="uuid",
        many=False,
        queryset=Customer.objects.all(),
    )

    class Meta:
        model = Customer
        fields = (
            "uuid",
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
            "uuid",
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
