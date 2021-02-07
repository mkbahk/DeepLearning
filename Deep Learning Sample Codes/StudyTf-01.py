# Tensorflow 2.0 이상

import tensorflow as tf
print(tf.__version__)

hello = tf.constant("Hello, TensorWorld!!!")

print(hello)

print(hello.numpy())