from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView

from .models import Customer


# Create your views here.
class HomePage(TemplateView):
    template_name = "home.html"


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "dashboard.html"
    # paginate_by = 10


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = "customer_detail.html"


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = "customer_form.html"
    fields = (
        "dba",
        "name",
        "billing_address",
        "shipping_address",
        "start_date",
        "end_date",
        "created_by",
        "active",
        "customer_type",
    )

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["create_customer"] = True

        return context


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    template_name = "customer_form.html"
    fields = (
        "dba",
        "name",
        "billing_address",
        "shipping_address",
        "start_date",
        "end_date",
        "created_by",
        "active",
        "customer_type",
    )


class AddressCreateView(LoginRequiredMixin, CreateView):
    pass


class AddressUpdateView(LoginRequiredMixin, UpdateView):
    pass
