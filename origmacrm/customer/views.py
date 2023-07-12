from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView

from .forms import CustomerForm
from .mixins import CustomerSingleObjectMixin
from .models import Address, Customer


# Create your views here.
class HomePage(TemplateView):
    template_name = "index.html"


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "dashboard.html"
    # paginate_by = 10


class CustomerDetailView(LoginRequiredMixin, CustomerSingleObjectMixin, DetailView):
    model = Customer
    template_name = "customer_detail.html"


class CustomerCreateView(LoginRequiredMixin, CustomerSingleObjectMixin, CreateView):
    form_class = CustomerForm
    template_name = "customer_test_form.html"


class CustomerUpdateView(LoginRequiredMixin, CustomerSingleObjectMixin, UpdateView):
    form_class = CustomerForm
    template_name = "customer_test_form.html"


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
