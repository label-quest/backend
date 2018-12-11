from django.http import HttpResponse
import json


def index(request):
    if request.method == 'GET':

        data = json.loads(request.body.decode('utf-8'))

        if not 'cust_id' in data:
            return HttpResponse(status=422)

        customer_id = data['cust_id']
        data_sets = get_data_sets(customer_id)

        return HttpResponse(json.dumps(data_sets), content_type="application/json", status=200)

    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        if not ('cust_id' in data and 'goal' in data and 'image_tar' in data):
            return HttpResponse(status=422)

        customer_id = data['cust_id']
        goal = data['goal']
        image_tar = data['image_tar']  # request.FILES['image_tar']

        return HttpResponse(json.dumps(data), content_type="application/json", status=200)

    else:
        return HttpResponse(status=404)


def get_data_sets(customer_id):
    data_set_1 = {
        'id': 1,
        'name': 'Data Set A',
        'goal': 'Distinguish between cats and dogs'
    }

    data_set_2 = {
        'id': 2,
        'name': 'Data Set B',
        'goal': 'Object detection for vehicles'
    }

    data_sets = [data_set_1, data_set_2]

    return data_sets
