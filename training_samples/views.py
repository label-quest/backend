from django.http import HttpResponse
import json


def index(request):
    if request.method != 'GET':
        return HttpResponse(status=404)

    labels = [
        {
            'id': 1,
            'name': 'LABEL_NAME_1',
        },
        {
            'id': 2,
            'name': 'LABEL_NAME_2',
        }
    ]

    image = {
        'id': 1,
        'imageSrc': 'https://images.sftcdn.net/images/t_app-cover-l,f_auto/p/ce2ece60-9b32-11e6-95ab-00163ed833e7/260663710/the-test-fun-for-friends-screenshot.jpg'
    }

    response_data = {
        'labels': labels,
        'image': image
    }

    response = HttpResponse(json.dumps(response_data), content_type="application/json", status=200)

    return response
