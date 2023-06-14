from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView

from .models import Customer


# Create your views here.
class HomePage(TemplateView):
    template_name = "home.html"


class CustomerListView(ListView):
    model = Customer
    template_name = "dashboard.html"
    # paginate_by = 10


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customer_detail.html"


class CustomerCreateView(CreateView):
    model = Customer
    template_name = "customer_form.html"


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = "customer_form.html"


class AddressCreateView(CreateView):
    pass


class AddressUpdateView(UpdateView):
    pass
