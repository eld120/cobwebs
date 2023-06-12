from django.conf import settings
from django.db import models

# Create your models here.

ACTIVE_OPTIONS = (("active", "Active"), ("active", "Inactive"), ("active", "Archived"))


class TimeStampModel(models.Model):
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True
    )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Customer(TimeStampModel):
    INDUSTRY_OPTIONS = (
        ("agriculture", "Agriculture"),
        ("arts entertainment", "Arts & Entertainment"),
        ("construction", "Construction"),
        ("education", "Education"),
        ("energy", "Energy"),
        ("food", "Food & Hospitality"),
        ("finance", "Finance and Insurance"),
        ("healthcare", "Healthcare"),
        ("manufacturing", "Manufacturing"),
        ("mining", "Mining"),
        ("other", "Other Services"),
        ("services", "Professional, Scientific, and Tech Services"),
        ("real estate", "Real Estate"),
        ("retail", "Retail"),
        ("transportation", "Transportation & Logistics"),
        ("utilities", "Utilities"),
        ("wholesale", "Wholesale"),
    )

    dba = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    billing_address = models.ForeignKey(
        "Address", related_name="%(class)s_billing_address", on_delete=models.DO_NOTHING
    )
    shipping_address = models.ForeignKey(
        "Address",
        related_name="%(class)s_shipping_address",
        on_delete=models.DO_NOTHING,
    )
    active = models.CharField(choices=ACTIVE_OPTIONS, max_length=50)
    customer_type = models.CharField(choices=INDUSTRY_OPTIONS, max_length=100)


class Address(TimeStampModel):
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
