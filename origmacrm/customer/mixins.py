from django.views.generic.detail import SingleObjectMixin

from .models import ACTIVE_OPTIONS, Address, Customer


class CustomerSingleObjectMixin(SingleObjectMixin):
    def get_object(self):
        uuid = self.kwargs["uuid"]
        return Customer.objects.get(uuid=uuid)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        updates = {
            "is_update_view": "update" in self.request.path,
            "address_list": Address.objects.all(),
            "customer_types": (type[1] for type in Customer.INDUSTRY_OPTIONS),
            "active_flag": (type[1] for type in ACTIVE_OPTIONS),
        }
        context |= updates
        return context


# class CustomerFormDataMixin:
#     '''temporarily retiring this mixin as it may be redundant'''
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         updates = {
#             "is_update_view" : "update" in self.request.path,
#             "address_list" : Address.objects.all(),
#             "customer_types" : (type[1] for type in Customer.INDUSTRY_OPTIONS)
#         }
#         context |= updates
#         return context
