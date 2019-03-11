from rest_framework import viewsets, views, response
from .models import Image
from .serializers import ImageSerializer, TrainingSampleSerializer


class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class TrainingSampleView(views.APIView):

    def get(self, request, format=None):
        obj = Image.objects.order_by("?").first()
        obj = TrainingSampleSerializer(obj)

        return response.Response(obj.data)

    @classmethod
    def get_extra_actions(cls):
        return []
