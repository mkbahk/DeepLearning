# import
from tensorflow import keras
from tensorflow.python.keras.callbacks import TensorBoard #TensorBoard를 import합니다.
from time import time # Log를 만들때 사용합니다.

# Tensorboard Setting
# python  C:\Users\mkbah\AppData\Roaming\Python\Python38\site-packages\tensorboard\main.py --logdir="C:\Temp\tensorlogs"
# http://localhost:6006/

# from keras.datasets import mnist
# from keras.utils import to_categorical
# from keras import layers
# from keras import models

(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()

train_images = train_images.reshape(60000, 28, 28, 1)
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape(10000, 28, 28, 1)
test_images = test_images.astype('float32') / 255

train_labels = keras.utils.to_categorical(train_labels)
test_labels = keras.utils.to_categorical(test_labels)

model = keras.Sequential()

model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1), padding='same'))
model.add(keras.layers.MaxPool2D(2, 2))
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(keras.layers.MaxPool2D(2, 2))
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))

model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(10, activation='relu'))
print(model.summary)

tensorboard = TensorBoard(log_dir="c:\\Temp\\tensorlogs\\{}".format(time()))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5, batch_size=65, callbacks=[tensorboard])

test_loss, test_acc = model.evaluate(test_images, test_labels)

print(test_loss, test_acc)