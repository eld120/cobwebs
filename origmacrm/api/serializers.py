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
    shipping_addresses = serializers.HyperlinkedRelatedField(
        view_name="api:address-detail",
        lookup_field="uuid",
        many=True,
        queryset=Customer.objects.all(),
    )

    class Meta:
        model = Customer
        fields = (
            "uuid",
            "dba",
            "name",
            "billing_address",
            "shipping_addresses",
            "start_date",
            "end_date",
            "active",
            "customer_type",
        )


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    primary = serializers.ChoiceField(Address.PRIMARY_CHOICES)

    class Meta:
        model = Address
        fields = (
            "uuid",
            "primary",
            "name",
            "address_1",
            "address_2",
            "city",
            "state",
            "zip_code",
            "phone",
            "email",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
