import sys
sys.path.append("..")
from rest_framework import serializers
from .models import Image
from data_sets.models import DataSet
from data_sets.serializers import DataSetSerializer


class ImageSerializer(serializers.ModelSerializer):
    data_set = serializers.PrimaryKeyRelatedField(queryset=DataSet.objects.all())

    class Meta:
        model = Image
        fields = ('id', 'file_path', 'data_set')


class TrainingSampleSerializer(serializers.ModelSerializer):
    data_set = DataSetSerializer(read_only=True)

    class Meta:
        model = Image
        fields = ('id', 'file_path', 'data_set')
