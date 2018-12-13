import sys
sys.path.append("..")
from rest_framework import serializers
from .models import DataSet
from customers.models import Customer
from potential_labels.serializers import PotentialLabelSerializer


class DataSetSerializer(serializers.ModelSerializer):
    potential_labels = PotentialLabelSerializer(many=True, read_only=True, required=False)
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

    class Meta:
        model = DataSet
        fields = ('id', 'name', 'description', 'goal', 'folder_path', 'customer', 'potential_labels')
