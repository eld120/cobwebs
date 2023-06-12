from django.urls import path

from . import views

app_name = "customer"

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("dashboard/", views.CustomerListView.as_view(), name="dashboard"),
    path("<int:pk>/", views.CustomerDetailView.as_view(), name="customer_detail"),
]
