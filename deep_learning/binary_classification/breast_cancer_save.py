from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense, Dropout
import pandas as pd
import numpy as np

previsores = pd.read_csv('/home/gabriel/Documentos/lamia/deep_learning/binary_classification/entradas_breast.csv')
classe = pd.read_csv('/home/gabriel/Documentos/lamia/deep_learning/binary_classification/saidas_breast.csv')

previsores = previsores.values
classe = classe.values

classificador = Sequential()

classificador.add(Dense(units=8, activation='relu', kernel_initializer='normal', input_dim=30))

classificador.add(Dropout(0.2))
classificador.add(Dense(units=8, activation='relu', kernel_initializer='normal'))

classificador.add(Dropout(0.2))
classificador.add(Dense(units=1, activation='sigmoid'))

classificador.compile(optimizer='adam', loss='binary_crossentropy', metrics=['binary_accuracy'])

classificador.fit(previsores, classe, batch_size=10, epochs=100)

new_input = np.array([
    [1.812e+01, 1.051e+01, 1.252e+02, 1.023e+03, 1.205e-01, 2.808e-01,
     3.042e-01, 1.493e-01, 2.451e-01, 7.982e-02, 1.117e+03, 9.275e-01,
     8.712e+03, 1.556e+02, 6.461e-03, 4.946e-02, 5.415e-02, 1.609e-02,
     3.045e-02, 6.275e-03, 2.560e+01, 1.755e+01, 1.868e+02, 2.041e+03,
     1.644e-01, 6.718e-01, 7.181e-01, 2.676e-01, 4.643e-01, 1.201e-01]
])

res = classificador.predict(new_input)
print(res > 0.5)

with open('/home/gabriel/Documentos/lamia/deep_learning/binary_classification/output/classificador_breast.json', 'w') as f: # salva a estrutura da rede
    f.write(classificador.to_json())

classificador.save_weights('/home/gabriel/Documentos/lamia/deep_learning/binary_classification/output/classificador_breast.h5')
