import numpy as np
from pylab import *
from matplotlib import pyplot as plt

pageSpeeds = np.random.normal(30000, 1, 1000) # variável independente
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3 # variável dependente

plt.scatter(pageSpeeds, purchaseAmount)
plt.show()

###################################################################################################

from scipy import stats

slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)
# slope: coeficiente angular - taxa de mudança na variável
# dependente para cada unidade de mudança na variável independente

# intercept: intercepto da reta - valor esperado da
# variável dependente quando a variável independente é zero

# r_value: indica a força e direção da relação linear entre as variáveis onde 1=correlação positiva
# perfeita, -1=negativa perfeita e 0= ausência de correçação. Como estamos elevando ao quadrado na
# linha 29, utilizamos a escala de 1 a 0, onde 1 indica melhor ajuste do modelo aos dados

# p_value: indica a significância estatística da relação linear estimada

# std_err: é uma medida da precisão da estimativa do coeficiente angular,
# ou seja, avalia o quão confiável é a estimativa do coeficiente angular.

r_value ** 2

def predict(x): # função da reta
    return slope * x + intercept # y = ax + b

fitLine = predict(pageSpeeds) # atribuição da reta usando o pageseeds como argumento para a função predict

plt.scatter(pageSpeeds, purchaseAmount) # plot do gráfico
plt.plot(pageSpeeds, fitLine, c='r') # adicionando a reta ao gráfico
plt.show()
