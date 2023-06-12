from django.shortcuts import render
from django.views.generic import DetailView, ListView
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
