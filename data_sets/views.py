from rest_framework import viewsets
from .models import DataSet
from .serializers import DataSetSerializer
from rest_framework_extensions.mixins import NestedViewSetMixin


class DataSetView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer
