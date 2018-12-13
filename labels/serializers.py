import sys
sys.path.append("..")
from rest_framework import serializers
from .models import Label
from users.models import User
from images.models import Image
from potential_labels.models import PotentialLabel


class LabelSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    image = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all())
    potential_label = serializers.PrimaryKeyRelatedField(queryset=PotentialLabel.objects.all())

    class Meta:
        model = Label
        fields = ('id', 'x_pos', 'y_pos', 'image', 'user', 'potential_label')
