from customer.models import Address, Customer
from rest_framework import mixins, permissions, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from user.models import User

from .mixins import CustomerSingleObjectMixin
from .serializers import AddressSerializer, CustomerSerializer, UserSerializer


class AddressViewset(
    CustomerSingleObjectMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """returns all addresses"""

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = [
        SessionAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "uuid"


class CustomerViewset(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [
        SessionAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "uuid"


class UserViewset(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [
        SessionAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]
