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
    #     self.fields['created_by'].queryset = Customer.objects.filter(user=self.request.user)

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
