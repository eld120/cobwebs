from django.urls import path

from . import views

app_name = "customer"

urlpatterns = [
    path("dashboard/", views.CustomerListView.as_view(), name="dashboard"),
    path(
        "customer-update/<int:pk>",
        views.CustomerUpdateView.as_view(),
        name="customer_update",
    ),
    path(
        "customer/<int:pk>/", views.CustomerDetailView.as_view(), name="customer_detail"
    ),
    path("customer/", views.CustomerCreateView.as_view(), name="customer_create"),
    path("", views.HomePage.as_view(), name="home"),
]
