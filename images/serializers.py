import sys
sys.path.append("..")
from rest_framework import serializers
from .models import Image
from data_sets.models import DataSet


class ImageSerializer(serializers.ModelSerializer):
    data_set = serializers.PrimaryKeyRelatedField(queryset=DataSet.objects.all())

    class Meta:
        model = Image
        fields = ('id', 'file_path', 'data_set')
