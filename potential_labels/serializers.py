import sys
sys.path.append("..")
from rest_framework import serializers
from .models import PotentialLabel
from data_sets.models import DataSet


class PotentialLabelSerializer(serializers.ModelSerializer):
    data_set = serializers.PrimaryKeyRelatedField(queryset=DataSet.objects.all())

    class Meta:
        model = PotentialLabel
        fields = ('id', 'name', 'description', 'data_set')
