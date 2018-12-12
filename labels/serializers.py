from rest_framework import serializers
from .models import Label


class LabelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Label
        fields = ('id', 'x_pos', 'y_pos', 'image', 'user', 'potential_label')
