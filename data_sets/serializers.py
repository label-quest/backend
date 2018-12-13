import sys
sys.path.append("..")
from rest_framework import serializers
from .models import DataSet
from customers.models import Customer


class DataSetSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

    class Meta:
        model = DataSet
        fields = ('id', 'name', 'description', 'goal', 'folder_path', 'customer')
