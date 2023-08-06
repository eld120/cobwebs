from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic.detail import SingleObjectMixin

from .models import ACTIVE_OPTIONS, Address, Customer


class CustomerSingleObjectMixin(SingleObjectMixin):
    """Enables Django to retrieve Addresses/Customers via their UUID rather than pk"""

    def get_object(self):
        uuid = self.kwargs["uuid"]
        if "address" in self.request.path:
            return get_object_or_404(Address, uuid=uuid)
        return get_object_or_404(Customer, uuid=uuid)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        updates = {
            "is_update_view": "update" in self.request.path,
            "address_list": get_list_or_404(Address),
            "customer_types": (type[1] for type in Customer.INDUSTRY_OPTIONS),
            "active_flag": (type[1] for type in ACTIVE_OPTIONS),
        }
        context |= updates
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CustomerLoginRequiredMixin(LoginRequiredMixin):
    """redirects users to the correct login page"""

    login_url = "user:login"


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
