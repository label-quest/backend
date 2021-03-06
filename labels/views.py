from rest_framework import viewsets, views, response
from rest_framework.decorators import api_view
from .models import Label
from .serializers import LabelSerializer


class LabelView(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelPlacementView(views.APIView):

    @api_view(['POST'])
    def create_label_placement(request):
        request_data = request.data
        print(request_data)
        if 'user_id' in request_data.keys() and 'image_id' in request_data.keys() and 'placed_labels' in request_data.keys():
            user_id = request_data['user_id']
            image_id = request_data['image_id']
            placed_labels = request_data['placed_labels']

            for placed_label in placed_labels:
                potential_label_id = placed_label['id']
                x_pos = placed_label['x']
                y_pos = placed_label['y']
                label = Label(potential_label_id=potential_label_id, x_pos=x_pos, y_pos=y_pos, user_id=user_id, image_id=image_id)
                label.save()

            return response.Response(status=200)
        else:
            return response.Response(status=422)

    @classmethod
    def get_extra_actions(cls):
        return []
