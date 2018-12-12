from rest_framework import serializers
from .models import PotentialLabel


class PotentialLabelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PotentialLabel
        fields = ('id', 'name', 'description')
