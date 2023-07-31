from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.bootstrap import Modal, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Row, Submit
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Address, Customer


class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FloatingField("dba"),
            FloatingField("name"),
            Row(
                Div(
                    FloatingField("billing_address"),
                    StrictButton(
                        "",
                        css_class="btn-tertiary input-group-text add-btn",
                        data_bs_toggle="modal",
                        data_bs_target="#createAddressModal",
                    ),
                    StrictButton(
                        "",
                        css_class="btn-tertiary input-group-text edit-btn",
                        css_id="billingAddressButton",
                        data_bs_toggle="modal",
                        data_bs_target="#createAddressModal",
                    ),
                    css_class="input-group input-group-sm mb-2",
                )
            ),
            Row(
                Div(
                    FloatingField("shipping_address"),
                    StrictButton(
                        "",
                        css_class="btn-tertiary input-group-text add-btn",
                        data_bs_toggle="modal",
                        data_bs_target="#createAddressModal",
                    ),
                    StrictButton(
                        "",
                        css_class="btn-tertiary input-group-text edit-btn",
                        css_id="shippingAddressButton",
                        data_bs_toggle="modal",
                        data_bs_target="#createAddressModal",
                    ),
                    css_class="input-group input-group-sm mb-2",
                )
            ),
            FloatingField("start_date"),
            FloatingField("end_date"),
            FloatingField("active"),
            FloatingField("customer_type"),
            StrictButton("Submit", css_class="btn-primary", type="submit"),
        )

    class Meta:
        model = Customer
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
        # widgets = {
        #     "start_date": AdminDateWidget(),  # Not working with crispy-forms thus far
        #     "end_date" : AdminDateWidget(),   # Not working with crispy-forms thus far
        # }


class AddressForm(forms.ModelForm):
    """Currently not used - all Addresses are updated via a serializer/viewset for end users"""

    class Meta:
        model = Address
        fields = (
            "address_1",
            "address_2",
            "city",
            "state",
            "zip_code",
            "phone",
            "email",
            "start_date",
            "end_date",
        )
