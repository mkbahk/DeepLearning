import tensorflow as tf
print(tf.__version__)

# X와 Y 데이타
x_train = [1, 2, 3]
y_train = [1, 2, 3]

W = tf.Variable(tf.random.normal([1]), name = 'Weight')
b = tf.Variable(tf.random.normal([1]), name = 'bias')

hypothesis = x_train * W + b

# cost / Loss function

cost = tf.reduce_mean(tf.square(hypothesis - y_train))

print("Weight --> \n", W)
print("bias --> \n", b)
print("cost --> \n", cost)

#GradientDescent
optimizer = tf.train.GradientDescent()
train = optimizer.minimize(cost)

print("Weight --> \n", W)
print("bias --> \n", b)
print("cost --> \n", cost)