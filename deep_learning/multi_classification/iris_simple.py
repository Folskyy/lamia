import pandas as pd
import numpy as np

base = pd.read_csv('iris.csv')

# o iloc é conveniente para usar indices inteiros (não indices rotulados)
previsores = base.iloc[:, 0:4].values
# pega o indice 4, pois não está trabalhando com intervalos
classe = base.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder
# transforma atributos categóricos para numéricos
label_encoder = LabelEncoder()
classe = label_encoder.fit_transform(classe)

from keras.utils import to_categorical
# transforma as classes para um formato binário
classe_dummy = to_categorical(classe)

from keras.layers import Dense # , Dropout
from keras.models import Sequential
from sklearn.model_selection import train_test_split

previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe_dummy, test_size=0.25)

classificador = Sequential()

classificador.add(Dense(units=4, activation='relu', input_dim=4))
classificador.add(Dense(units=4, activation='relu'))
classificador.add(Dense(units=3, activation='softmax')) # função ideal para classificações multiplas

classificador.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
classificador.fit(previsores_treinamento, classe_treinamento, batch_size=10, epochs=1000)

resultado = classificador.evaluate(previsores_teste, classe_teste)
previsoes = classificador.predict(previsores_teste)
previsoes = previsoes > 0.5

# transformação das colunas para categorias (para criar a matriz de confusão)
classe_teste2 = [np.argmax(t) for t in classe_teste]
previsoes2 = [np.argmax(t) for t in previsoes]

from sklearn.metrics import confusion_matrix
matriz = confusion_matrix(previsoes2, classe_teste2)
matriz