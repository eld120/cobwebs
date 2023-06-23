from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView

from .mixins import CustomerSingleObjectMixin
from .models import Address, Customer


# Create your views here.
class HomePage(TemplateView):
    template_name = "home.html"


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "dashboard.html"
    # paginate_by = 10


class CustomerDetailView(LoginRequiredMixin, CustomerSingleObjectMixin, DetailView):
    model = Customer
    template_name = "customer_detail.html"


class CustomerCreateView(LoginRequiredMixin, CustomerSingleObjectMixin, CreateView):
    model = Customer
    template_name = "customer_form.html"
    fields = (
        "dba",
        "name",
        "billing_address",
        "shipping_address",
        "start_date",
        "end_date",
        "active",
        "customer_type",
    )


class CustomerUpdateView(LoginRequiredMixin, CustomerSingleObjectMixin, UpdateView):
    model = Customer
    template_name = "customer_form.html"
    fields = (
        "dba",
        "name",
        "billing_address",
        "shipping_address",
        "start_date",
        "end_date",
        "active",
        "customer_type",
    )


class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    template_name = "address_form.html"
    fields = (
        "address_1",
        "address_2",
        "city",
        "state",
        "zip_code",
        "phone",
        "email",
    )


class AddressUpdateView(LoginRequiredMixin, CustomerSingleObjectMixin, UpdateView):
    model = Address
    template_name = "address_form.html"
    fields = (
        "address_1",
        "address_2",
        "city",
        "state",
        "zip_code",
        "phone",
        "email",
    )
