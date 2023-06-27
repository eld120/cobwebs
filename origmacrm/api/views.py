from customer.models import Address, Customer
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from user.models import User

from .serializers import AddressSerializer, CustomerSerializer, UserSerializer


class AddressViewset(viewsets.ModelViewSet):
    """returns all addresses"""

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "uuid"

    # @action(detail=True, methods=['POST'], url_path='update-address', url_name='update_address')
    # def update_address(self, request, uuid=None):
    #     address = self.get_object()


class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "uuid"


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
