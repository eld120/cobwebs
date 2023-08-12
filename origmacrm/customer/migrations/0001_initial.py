# Generated by Django 4.2.3 on 2023-08-12 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "active",
                    models.CharField(
                        choices=[
                            ("active", "Active"),
                            ("inactive", "Inactive"),
                            ("archived", "Archived"),
                        ],
                        max_length=50,
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                (
                    "primary",
                    models.CharField(
                        blank=True,
                        choices=[("y", "Yes"), ("n", "No")],
                        default="n",
                        max_length=3,
                    ),
                ),
                ("name", models.CharField(max_length=70)),
                ("address_1", models.CharField(max_length=70)),
                ("address_2", models.CharField(blank=True, max_length=70, null=True)),
                ("city", models.CharField(max_length=30)),
                ("state", models.CharField(max_length=20)),
                ("zip_code", models.CharField(max_length=20)),
                ("phone", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=50)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "active",
                    models.CharField(
                        choices=[
                            ("active", "Active"),
                            ("inactive", "Inactive"),
                            ("archived", "Archived"),
                        ],
                        max_length=50,
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("dba", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                (
                    "customer_type",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "billing_address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="%(class)s_billing_address",
                        to="customer.address",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CustomerShippingRelationship",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="customer.customer",
                    ),
                ),
                (
                    "shipping_addresses",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="customer.address",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customer",
            name="shipping_addresses",
            field=models.ManyToManyField(
                related_name="%(class)s_shipping_addresses",
                through="customer.CustomerShippingRelationship",
                to="customer.address",
            ),
        ),
    ]
