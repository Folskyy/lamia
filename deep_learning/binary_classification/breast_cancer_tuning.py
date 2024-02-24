from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense, Dropout
import pandas as pd
import keras

previsores = pd.read_csv('/home/gabriel/Documentos/lamia/deep_learning/binary_classification/entradas_breast.csv')
classe = pd.read_csv('/home/gabriel/Documentos/lamia/deep_learning/binary_classification/saidas_breast.csv')

def criar_rede(optimizer, loss, kernel_init, activation, neurons):
    classificador = Sequential()

    classificador.add(Dense(units=neurons, activation=activation, kernel_initializer=kernel_init, input_dim=30))
    classificador.add(Dropout(0.1))
    classificador.add(Dense(units=neurons, activation=activation, kernel_initializer=kernel_init))
    classificador.add(Dropout(0.1))
    classificador.add(Dense(units=1, activation='sigmoid'))

    classificador.compile(optimizer=optimizer, loss=loss, metrics=['binary_accuracy'])
    
    return classificador

# build_fn: função de criação da rede neural
classificador =  KerasClassifier(build_fn=criar_rede)

parametros = {'batch_size': [10, 30],
              'epochs': [25, 50],
              'optimizer': ['Adam', 'sgd'],
              'loss': ['binary_crossentropy', 'hinge'],
              'kernel_init': ['random_uniform', 'normal'],
              'activation': ['relu', 'tanh'],
              'neurons': [16, 8]}
grid_search = GridSearchCV(estimator=classificador, param_grid=parametros, scoring='accuracy', cv=5)
grid_search = grid_search.fit(previsores, classe)

melhores_parametros = grid_search.best_params_
melhor_precisao = grid_search.best_score_

# refaz o modelo com os parametros de melhor score para a versão final
# para fazer o teste com uma nova entrada, usa-se **classificador.predict(nova_entrada)**
# para salvar o modelo:
# classificador_json = classificado.to_json()
# with open('classificador_json', 'w') as json_file:
#   json_file.write(classificador_json) --> estrutura da rede
# classificador.save_weights('classificador_breasts.h5) --> pesos dos neuronios
