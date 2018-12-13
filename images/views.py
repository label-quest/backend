from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer, TrainingSampleSerializer
import random


class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class TrainingSample(viewsets.ModelViewSet):
    images_count = Image.objects.all().count()
    random_index = random.randint(0, images_count - 1)
    print("RANDOM: {}".format(random_index))

    queryset = Image.objects.order_by("?")
    serializer_class = TrainingSampleSerializer
