# Generated by Django 4.2.2 on 2023-06-12 02:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0002_alter_timestampmodel_created_on_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timestampmodel",
            name="end_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
