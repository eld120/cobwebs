from django.db import models

# Create your models here.
class TimeStampModel:
    created_on = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated_on = models.DateTimeField(auto_now=False, auto_now_add=False)

class Customer:
    name = models.CharField(max_length=50)
    dba  = models.CharField(max_length=50)
