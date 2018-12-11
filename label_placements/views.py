from django.http import HttpResponse
import json


def index(request):
    if request.method != 'POST':
        return HttpResponse(status=404)

    data = json.loads(request.body.decode('utf-8'))

    if not ('user_id' in data and 'image_id' in data and 'labels' in data):
        return HttpResponse(status=422)

    user_id = data['user_id']
    image_id = data['image_id']
    labels = data['labels']  # [{'id': LABEL_ID_1, point: [x, y]}, {'id': LABEL_ID_1, point: [x, y]}]

    response = HttpResponse(json.dumps(data), content_type="application/json", status=200)

    return response
