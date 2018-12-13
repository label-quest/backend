from rest_framework import viewsets
from .models import PotentialLabel
from .serializers import PotentialLabelSerializer


class PotentialLabelView(viewsets.ModelViewSet):
    queryset = PotentialLabel.objects.all()
    serializer_class = PotentialLabelSerializer
