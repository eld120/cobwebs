from django.urls import path

from . import views

app_name = "customer"

urlpatterns = [
    path("dashboard/", views.CustomerListView.as_view(), name="dashboard"),
    path(
        "customer-update/<str:uuid>",
        views.CustomerUpdateView.as_view(),
        name="customer_update",
    ),
    path(
        "customer/<str:uuid>/",
        views.CustomerDetailView.as_view(),
        name="customer_detail",
    ),
    path("customer/", views.CustomerCreateView.as_view(), name="customer_create"),
    path(
        "address-update/<str:uuid>",
        views.AddressUpdateView.as_view(),
        name="address_update",
    ),
    path("address/", views.AddressCreateView.as_view(), name="address_create"),
    path("", views.HomePage.as_view(), name="home"),
]
