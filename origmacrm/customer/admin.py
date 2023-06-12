from django.contrib import admin
from .models import Customer, Address

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address, AddressAdmin)