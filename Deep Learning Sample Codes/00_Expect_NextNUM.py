### 문제의 정의
# 1~7을 학습해 다음 세자리 8, 9, 10을 예측하는 Deep Learning 예제
#

import numpy as np
from tensorflow import keras
from tensorflow.python.keras.callbacks import TensorBoard #TensorBoard를 사용할 수 있도록 관련 모듈 import합니다.
from time import time # Log를 만들때 파일이름을 시간으로 만들기 위함.

tensorboard = TensorBoard(log_dir="c:/Temp/tensorlogs/{}".format(time()))

### 훈련용 데이타 정의
# 배열생성
x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([1,2,3,4,5,6,7,8,9,10])

# 훈련용과 테스트용으로 나누기
x_train = x[:7]
y_train = y[:7]
x_test = x[7:]
y_test = y[7:]

### 모델생성 및 훈련
#모델 정의
model = keras.Sequential()
model.add(keras.layers.Dense(10, input_dim = 1, activation='relu')) #input layer
model.add(keras.layers.Dense(5, activation='relu'))  # hidden layer
model.add(keras.layers.Dense(1)) #output layer

#모델 컴파일
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'] )
model.summary()

#모델 [훈련training|학습Learning]
model.fit(x_train, y_train, epochs=300, batch_size=1, callbacks=[tensorboard]) #batch_size default값은 32임 여기서 반드시 1로 해야함

### 예측(추론Inference)
#모델에 테스트데이타 입력하여 예측(추론)
y_predict = model.predict(x_test)
print(np.round(y_predict))
