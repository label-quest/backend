from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework_extensions.mixins import NestedViewSetMixin


class CustomerView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
