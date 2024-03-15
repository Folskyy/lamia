#%%
import matplotlib.pyplot as plt
from keras.datasets import mnist # conjunto de dados para treinamento
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D # camadas estruturais de uma CNN
from keras.utils import np_utils

#%%
# comumente o x é usado como os dados de entrada
# e o y como as saídsa esperadas
(x_treinamento, y_treinamento), (x_teste, y_teste) = mnist.load_data()

#%%
# plot de uma imagem no conjunto de dados, o cmap altera a escala de cores do plot
i = 4
plt.imshow(x_teste[i], cmap='tab20')
plt.title('Classe ' + str(y_teste[i]))

#%%
# Simplifica o processamento (reduzindo os dados de entrada em 2/3) convertendo
# as entradas de RGB para tons de cinza.
# Técnica somente válida quando a cor e textura não importam.
previsores_treinamento = x_treinamento.reshape(x_treinamento.shape[0], 28, 28, 1)
previsores_teste = x_teste.reshape(x_teste.shape[0], 28, 28, 1)
#%%
# conversão dos valores de uint32 para float32 com o intuito de aumentar a precisão
previsores_treinamento = previsores_treinamento.astype('float32')
previsores_teste = previsores_teste.astype('float32')

#%%
# Uso do MinMax Normalization
# evisores_treinamento_normalizado = (previsores_treinamento - min(previsores_treinamento)) / (max(previsores_treinamento) - min(previsores_treinamento))
previsores_treinamento /= 255
previsores_teste /= 255

#%%
# transforma os dados de saída (resultados) para um formato categórico
# vetor binário onde a posição que possui 1 é a categoria que o objeto se encaixa
classe_treinamento = np_utils.to_categorical(y_treinamento, 10)
classe_teste = np_utils.to_categorical(y_teste, 10)

classificador = Sequential()
classificador.add(Conv2D(filters=64, kernel_size=(3, 3), input_shape=(28, 28, 1), activation='relu'))
classificador.add(MaxPooling2D(pool_size=(2,2)))
classificador.add(Flatten())

#%%
classificador.add(Dense(units=128, activation='relu'))
classificador.add(Dense(units=10, activation='softmax'))
classificador.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
classificador.fit(previsores_treinamento, classe_treinamento, batch_size=128, epochs=5, validation_data=(previsores_teste, classe_teste))
pi
#%%
resultado = classificador.evaluate(previsores_teste, classe_teste)

#%%
from PIL import Image
import numpy as np

def to_nparray(image_path):
    image = Image.open(image_path)
    
    # image = image.resize(target_size)
    
    image_array = np.array(image)
    
    return image_array

path = 'Documentos/lamia/convolutional_neural_network/input/nove.png'

png_input = to_nparray(path)


classificador.summary()