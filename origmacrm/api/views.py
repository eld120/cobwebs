from customer.models import Address, Customer
from rest_framework import permissions, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from user.models import User

from .mixins import CustomerSingleObjectMixin
from .serializers import AddressSerializer, CustomerSerializer, UserSerializer


class AddressViewset(CustomerSingleObjectMixin, viewsets.ModelViewSet):
    """returns all addresses"""

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    authentication_classes = [
        SessionAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "uuid"


class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [
        SessionAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "uuid"


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [
        SessionAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated]
