# import
from tensorflow import keras
from tensorflow.python.keras.callbacks import TensorBoard #TensorBoard를 import합니다.
from time import time # Log를 만들때 사용합니다.

# Tensorboard Setting
# python c:\Users\bernhard.hiller\AppData\Roaming\Python\Python37\site-packages\tensorboard\main.py --logdir="c:\Temp\tensorlogs"
# http://localhost:6006/


# load Data
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()


for i in range(5):
    print(y_train[i])

# one-hot enconding
# 5 --> [0,0,0,0,0,1,0,0,0,0]
# 1 --> [0,1,0,0,0,0,0,0,0,0]
#
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

for i in range(5):
    print(y_train[i])


x_train = x_train.reshape([60000, 28*28])
x_test = x_test.reshape([10000, 28*28])

print(y_train.shape, y_test.shape)
print(x_train.shape, x_test.shape)

model = keras.Sequential()
model.add(keras.layers.Dense(128, activation="sigmoid", input_shape=(28*28,)))
model.add(keras.layers.Dense(128, activation="sigmoid"))
model.add(keras.layers.Dense(10,activation="sigmoid"))

optimizer = keras.optimizers.SGD(learning_rate=0.1)
model.compile(optimizer=optimizer, loss="categorical_crossentropy", metrics=['accuracy'])
model.summary()

tensorboard = TensorBoard(log_dir="c:/Temp/tensorlogs/{}".format(time()))


print("\n Starting Training...")
model.fit(x_train, y_train, batch_size=128, epochs=100, validation_data=(x_test, y_test), callbacks=[tensorboard])
print("\n Finished Training...")

print("\n Evaulating...")
model.evaluate(x_test, y_test)
print("\n Job Finished...")