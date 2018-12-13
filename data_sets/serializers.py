from rest_framework import serializers
from .models import DataSet


class DataSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataSet
        fields = ('id', 'name', 'description', 'goal', 'folder_path', 'customer_id', 'potential_label_id')
