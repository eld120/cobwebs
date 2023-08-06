from typing import Any, Dict

from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView

from .forms import CustomerForm
from .mixins import CustomerLoginRequiredMixin as LoginRequiredMixin
from .mixins import CustomerSingleObjectMixin as SingleObjectMixin
from .models import Address, Customer


# Create your views here.
class HomePage(TemplateView):
    """Homepage for all users"""

    template_name = "index.html"


class CustomerListView(LoginRequiredMixin, ListView):
    """Homepage for authenticated users"""

    model = Customer
    template_name = "dashboard.html"
    # paginate_by = 10


class CustomerDetailView(LoginRequiredMixin, SingleObjectMixin, DetailView):
    model = Customer
    template_name = "customer/customer_detail.html"


class CustomerCreateView(LoginRequiredMixin, SingleObjectMixin, CreateView):
    form_class = CustomerForm
    template_name = "customer/customer_test_form.html"


class CustomerUpdateView(LoginRequiredMixin, SingleObjectMixin, UpdateView):
    form_class = CustomerForm
    template_name = "customer/customer_test_form.html"


class AddressCreateView(LoginRequiredMixin, CreateView):
    """Unused view currently - Addresses are created via an API for end users"""

    model = Address
    template_name = "customer/address_form.html"
    fields = (
        "address_1",
        "address_2",
        "city",
        "state",
        "zip_code",
        "phone",
        "email",
    )


class AddressUpdateView(LoginRequiredMixin, SingleObjectMixin, UpdateView):
    """Unused view currently - Addresses are updated via an API for end users"""

    model = Address
    template_name = "customer/address_form.html"
    fields = (
        "address_1",
        "address_2",
        "city",
        "state",
        "zip_code",
        "phone",
        "email",
    )
