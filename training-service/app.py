from flask import Flask, jsonify, request
import requests
import skimage
import numpy as np
from PIL import Image
from io import BytesIO
import pandas as pd

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

from model import Model

app = Flask(__name__)

models = {}
classes = {}
number_classes = {}
new_shape = (100, 100, 3)

# Instantiates a client
client = vision.ImageAnnotatorClient()


@app.route('/classify', methods=['GET'])
def classify():
    global classes

    file_path = request.args.get('file_path')
    dataset = request.args.get('dataset')

    picture = requests.get(file_path).content

    if dataset not in models:
        image = types.Image(content=picture)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations
        descriptions = []
        for label in labels:
            descriptions.append(label.description)

        return jsonify({'descriptions': descriptions})
    else:
        image = Image.open(BytesIO(picture))
        content = skimage.transform.resize(np.array(image), new_shape)
        predictions = models[dataset].predict(np.reshape(content, (1, new_shape[0], new_shape[1], new_shape[2])))
        return jsonify({'descriptions': [x for _, x in sorted(zip(predictions.tolist()[0], classes[dataset]))]})

@app.route('/train', methods=['POST'])
def train():
    global classes
    global number_classes

    content = request.get_json()
    print(content['data'])

    x = []
    y = []
    for datapoint in content['data']:
        picture = requests.get(datapoint['file_path']).content
        image = Image.open(BytesIO(picture))
        x.append(np.array(image))
        y.append(datapoint['label'])

    x = [skimage.transform.resize(image, new_shape) for image in x]

    classes[content['dataset']] = set(y)

    x = np.array(x)
    y = pd.get_dummies(y).as_matrix()

    model = Model(len(classes[content['dataset']]))
    model.fit(x, y)
    models[content['dataset']] = model
    return jsonify("200")


if __name__ == '__main__':
    app.run(debug=True)
