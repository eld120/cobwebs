from django.contrib import admin

from .models import Address, Customer, CustomerShippingRelationship


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    pass


class CustomerShippingRelationshipAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(CustomerShippingRelationship, CustomerShippingRelationshipAdmin)
