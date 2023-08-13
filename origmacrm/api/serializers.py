from customer.models import Address, Customer
from rest_framework import serializers, validators
from user.models import User


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    billing_address = serializers.HyperlinkedRelatedField(
        view_name="api:address-detail",
        lookup_field="uuid",
        many=False,
        queryset=Address.objects.all(),
    )
    shipping_addresses = serializers.HyperlinkedRelatedField(
        view_name="api:address-detail",
        lookup_field="uuid",
        many=True,
        queryset=Address.objects.all(),
    )
    created_by = serializers.HyperlinkedRelatedField(
        view_name="user:user_detail",
        lookup_field="pk",
        many=False,
        queryset=User.objects.all(),
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
            "created_by",
        )
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Customer.objects.all(),
                fields=(
                    "dba",
                    "name",
                ),
            )
        ]


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    primary = serializers.ChoiceField(Address.PRIMARY_CHOICES)
    created_by = serializers.HyperlinkedRelatedField(
        view_name="user:user_detail",
        lookup_field="pk",
        many=False,
        queryset=User.objects.all(),
    )

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
            "start_date",
            "end_date",
            "active",
            "created_by",
        )

        class Meta:
            validators = [
                validators.UniqueTogetherValidator(
                    queryset=Address.objects.all(),
                    fields=(
                        "address_1",
                        "address_2",
                        "city",
                        "state",
                        "zip_code",
                    ),
                )
            ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "last_login",
            "is_superuser",
            "username",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
            "name",
        )
