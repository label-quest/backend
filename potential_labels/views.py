from rest_framework import viewsets
from .models import PotentialLabel
from .serializers import PotentialLabelSerializer
from rest_framework_extensions.mixins import NestedViewSetMixin


class PotentialLabelView(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = PotentialLabel.objects.all()
    serializer_class = PotentialLabelSerializer
