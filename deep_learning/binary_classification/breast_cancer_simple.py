import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

import keras
from keras.models import Sequential
from keras.layers import Dense

previsores = pd.read_csv('/home/gabriel/Documentos/lamia/deep_learning/binary_classification/entradas_breast.csv')
classe = pd.read_csv('/home/gabriel/Documentos/lamia/deep_learning/binary_classification/saidas_breast.csv')

# função automatica para fazer a divisao dos dados treinamento/teste
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.25)

classificador = Sequential()

# ==========PARAMETROS=========
# Sequential.add(): Adiciona camadas ao modelo sequencial, nesse caso, uma camada densa
# units: quantidade de neurônios na camada oculta. Fórmula para usada: (num de entradas + num de saidas) / *2* *por ser uma classificação binária*
# activation: Função de ativação
# kernel_initializer: Inicialização dos pesos
# input_dim: Número de elementos na camada de entrada / quant. de atributos do arquivo de entrada (ex: colunas de um csv)
classificador.add(Dense(units = 16, activation = 'relu', kernel_initializer = 'random_uniform', input_dim = 30))
classificador.add(Dense(units = 16, activation = 'relu', kernel_initializer = 'random_uniform'))
classificador.add(Dense(units = 1, activation = 'sigmoid'))

# keras.optimizers.Adam(): invoca um otimizador 'Adam' (algoritmo que iterativamente adapta a taxa de aprendizado).
# lr: taxa de aprendizagem
# decay: taxa de decaimento do learning_rate ao longo do treinamento
# clipvalue: limitação do gradiente (x até -x)
otimizador = keras.optimizers.Adam(lr = 0.001, decay = 0.0001, clipvalue = 0.5)

# ==========PARAMETROS==========
# Sequential.compile(): configura o modelo para o treinamento
# optimizer: Função otimizadora (pode adaptar uma ou usar uma default)
# loss: Função de perda(cálculo do erro) Ex: Mean Square Error, Mean Absolute Error... O binary_crossentropy é para classificações binárias
# metrics: Medida(s) que voce deseja para avaliar o desempenho do modelo
classificador.compile(optimizer = otimizador, loss = 'binary_crossentropy', metrics = ['binary_accuracy'])

# ==========PARAMETROS==========
# Sequential.fit(): treina o modelo compilado no conjunto de dados fornecido.  "encaixa o modelo nos dados"
# batch_size: Tamanho do lote (quantos exemplos do treinamentos são considerados em uma atualização do gradiente)
# epochs: Número de vezes em que o modelo verá todo o conjunto de dados
classificador.fit(previsores_treinamento, classe_treinamento, batch_size = 10, epochs = 100)

# faz previsões com base nos dados que não foram utilizados no treinamento 'fit()'
previsoes = classificador.predict(previsores_teste)

previsoes = (previsoes > 0.5)
previsoes

from sklearn.metrics import confusion_matrix, accuracy_score

# Precisão dp modelo
precisao = accuracy_score(classe_teste, previsoes)
# matriz de confusão
matriz = confusion_matrix(classe_teste, previsoes)

classe_teste
previsoes

precisao
matriz

# recebe uma nparray com os pesos de uma das camadas ocultas
# 16x16 da camada oculta + 1x16 do bias
peso0 = np.array(classificador.layers[0].get_weights())
peso1 = np.array(classificador.layers[1].get_weights())

print(f"Número de acertos: {(previsoes == classe_teste).sum()}")
print(f"Número de erros: {previsoes.size - (previsoes == classe_teste).sum()}")

peso0