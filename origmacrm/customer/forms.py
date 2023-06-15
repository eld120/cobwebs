from django import forms

from .models import Address, Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            "dba",
            "name",
            "billing_address",
            "shipping_address",
            "start_date",
            "end_date",
            "created_by",
            "active",
            "customer_type",
        )


class AddressForm(forms.ModelForm):
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
            "created_by",
        )
