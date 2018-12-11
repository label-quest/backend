from rest_framework import viewsets
from .models import DataSet
from .serializers import DataSetSerializer


class DataSetView(viewsets.ModelViewSet):
    queryset = DataSet.objects.all()
    serializer_class = DataSetSerializer
