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
    shipping_addresses_list = serializers.SerializerMethodField(
        method_name="get_shipping_addresses_list"
    )
    created_by = serializers.HyperlinkedRelatedField(
        view_name="user:user_detail",
        lookup_field="pk",
        many=False,
        queryset=User.objects.all(),
    )
    customer_type_options = serializers.SerializerMethodField(
        method_name="get_customer_industry_list"
    )
    active_options = serializers.SerializerMethodField(
        method_name="get_customer_active_list"
    )

    class Meta:
        model = Customer
        fields = (
            "uuid",
            "dba",
            "name",
            "billing_address",
            "shipping_addresses",
            "shipping_addresses_list",
            "start_date",
            "end_date",
            "active",
            "active_options",
            "customer_type",
            "customer_type_options",
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

    def get_shipping_addresses_list(self, obj):
        return obj.get_shipping_addresses()

    def get_customer_industry_list(self, obj):
        return obj.get_customer_industry_options()

    def get_customer_active_list(self, obj):
        return obj.get_customer_active_options()


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
