from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.bootstrap import Modal, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Row
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
                        "➕",
                        css_class="btn-tertiary input-group-text",
                    ),
                    css_class="input-group input-group-sm mb-2",
                    data_bs_toggle="modal",
                    data_bs_target="#createAddressModal",
                )
            ),
            Row(
                Div(
                    FloatingField("shipping_address"),
                    StrictButton(
                        "➕",
                        css_class="btn-tertiary input-group-text",
                    ),
                    css_class="input-group input-group-sm mb-2",
                    data_bs_toggle="modal",
                    data_bs_target="#createAddressModal",
                )
            ),
            FloatingField("start_date"),
            FloatingField("end_date"),
            FloatingField("active"),
            FloatingField("customer_type"),
            # Modal(
            #     FloatingField('address_1'),
            #     FloatingField('address_2'),
            #     FloatingField('city'),
            #     FloatingField('state'),
            #     FloatingField('zip_code'),
            #     FloatingField('phone'),
            #     FloatingField('email'),
            #     FloatingField('start_date'),
            #     FloatingField('end_date'),
            #     # we weant to prevent the submission of the modal/form on submit
            #     StrictButton("submit", "Submit", css_class="btn btn-primary")
            # ),
            StrictButton("submit", "Submit", css_class="btn btn-primary"),
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
