from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD


class Model:
    model = None

    def __init__(self, number_classes):
        self.model = Sequential()
        # input: 100x100 images with 3 channels -> (100, 100, 3) tensors.
        # this applies 32 convolution filters of size 3x3 each.
        self.model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)))
        self.model.add(Conv2D(32, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))

        self.model.add(Conv2D(64, (3, 3), activation='relu'))
        self.model.add(Conv2D(64, (3, 3), activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))

        self.model.add(Flatten())
        self.model.add(Dense(256, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(number_classes, activation='softmax'))

        sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
        self.model.compile(loss='categorical_crossentropy', optimizer=sgd)

    def fit(self, x_train, y_train, batch_size=32, epochs=10):
        self.model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs)

    def predict(self, image):
        return self.model.predict(image)
