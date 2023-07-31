import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse

ACTIVE_OPTIONS = (
    ("active", "Active"),
    ("inactive", "Inactive"),
    ("archived", "Archived"),
)


class TimeStampModel(models.Model):
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True
    )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # active = models.CharField(choices=ACTIVE_OPTIONS, max_length=50)


class Customer(TimeStampModel):
    """
    A class used to capture a business entity/billing account which may exist in
    one or more locations/addresses
    """

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
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    dba = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    billing_address = models.ForeignKey(
        "Address", related_name="%(class)s_billing_address", on_delete=models.DO_NOTHING
    )
    # shipping address should be a Many to Many relationship
    shipping_address = models.ForeignKey(
        "Address",
        related_name="%(class)s_shipping_address",
        on_delete=models.DO_NOTHING,
    )
    active = models.CharField(choices=ACTIVE_OPTIONS, max_length=50)
    customer_type = models.CharField(choices=INDUSTRY_OPTIONS, max_length=100)

    def __str__(self) -> str:
        return f"{self.name} dba {self.dba}"

    def get_absolute_url(self):
        return reverse("customer:customer_update", kwargs={"uuid": self.uuid})


class Address(TimeStampModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    address_1 = models.CharField(max_length=70)
    address_2 = models.CharField(max_length=70, blank=True, null=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)

    def __str__(self) -> str:
        return f"{self.address_1} {self.city} {self.state} {self.zip_code}"

    def get_absolute_url(self):
        return reverse("customer:address_update", kwargs={"uuid": self.uuid})

    def save(self, request=None, *args, **kwargs) -> None:
        if request:
            self.created_by = request.user
        super(Address, self).save(*args, **kwargs)
