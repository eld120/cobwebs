from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from django import forms

from .models import Address, Customer


class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            FloatingField("dba"),
            FloatingField("name"),
            FloatingField("billing_address"),
            FloatingField("shipping_address"),
            FloatingField("start_date"),
            FloatingField("end_date"),
            FloatingField("active"),
            FloatingField("customer_type"),
            Submit("submit", "Submit", css_class="btn btn-primary"),
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

    # def form_valid(self, form):
    #     customer_form = form.save(commit=False)
    #     customer_form.created_by = self.request.user
    #     customer_form.save()
    #     return super(CustomerForm, self ).form_valid(form)

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request')
    #     super(CustomerForm, self).__init__(*args, **kwargs)
    #     # self.fields['created_by'].queryset = Customer.objects.filter(user=self.request.user)
    #     self.fields['billing_address'].queryset = Address.objects.filter()

    # def save(self, *args, **kwargs):
    #     kwargs['commit']=False

    #     customer_form = super(CustomerForm, self).save(*args, **kwargs)
    #     print(f"{self.request}")
    #     if self.request:
    #         customer_form.created_by = self.request.user
    #     customer_form.save()
    #     return customer_form


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
        )
