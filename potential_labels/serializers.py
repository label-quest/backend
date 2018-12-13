import sys
sys.path.append("..")
from rest_framework import serializers
from .models import PotentialLabel


class PotentialLabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PotentialLabel
        fields = ('id', 'name', 'description')
