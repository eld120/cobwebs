from django.urls import include, path
from rest_framework import routers

from . import views

app_name = "api"

router = routers.DefaultRouter()
router.register(r"addresses", views.AddressViewset, basename="address")
router.register(r"users", views.UserViewset)
router.register(r"customers", views.CustomerViewset, basename="customer")


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
]
