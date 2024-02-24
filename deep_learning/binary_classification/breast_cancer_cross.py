from keras.wrappers.scikit_learn import KerasClassifier # recursos para a validação cruzada
from sklearn.model_selection import cross_val_score # recursos para a validação cruzada
from keras.models import Sequential
from keras.layers import Dense, Dropout
import pandas as pd
import keras

previsores = pd.read_csv('/home/gabriel/Documentos/lamia/deep_learning/binary_classification/entradas_breast.csv')
classe = pd.read_csv('/home/gabriel/Documentos/lamia/deep_learning/binary_classification/saidas_breast.csv')

def criar_rede():
    classificador = Sequential()

    # add de camadas ocultas e de saida
    classificador.add(Dense(units = 16, activation = 'relu', kernel_initializer = 'random_uniform', input_dim = 30))
    classificador.add(Dropout(0.1)) # zera 10% dos neuronios para evitar o overfiting
    classificador.add(Dense(units = 16, activation = 'relu', kernel_initializer = 'random_uniform'))
    classificador.add(Dropout(0.1)) # zera 10% dos neuronios da segunda camada para evitar o overfiting
    classificador.add(Dense(units = 1, activation = 'sigmoid'))

    otimizador = keras.optimizers.Adam(lr = 0.001, clipvalue = 0.5)

    classificador.compile(optimizer = otimizador, loss = 'binary_crossentropy', metrics = ['binary_accuracy'])
    
    return classificador

# build_fn: função de criação da rede neural
classificador =  KerasClassifier(build_fn=criar_rede, epochs=100, batch_size=10)

resultados = cross_val_score(estimator=classificador, X=previsores, y=classe, cv=10, scoring='accuracy')