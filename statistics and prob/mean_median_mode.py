import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ffigura 1
plt.figure(1)
renda = np.random.normal(27000, 15000, 10000) # distribuição gussiana: loc -> media da distrib; scale:-> desvio padrao; size -> formato da saída

np.mean(renda) # média
np.median(renda) # mediana

plt.hist(renda, 50)
plt.show()

# figura 2
plt.figure(2)
renda = np.append(renda, [1000000000]) # a função adiciona um nodo de 10⁷ na lista 'renda'

plt.hist(renda, 50)
np.mean(renda)
np.median(renda)

plt.show()


# moda
idades = np.random.randint(18, high=100, size=500)
stats.mode(idades) # retorna a moda e o número de recorrência da mesma



################################################## EXERCISES ##############################################


# %matplotlib inline -> só é necessário no jupyter notebook
import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 20.0, 10000)
plt.figure(3)
# plt.hist(incomes, 50)

# plt.show()

np.mean(incomes)
np.median(incomes) # makes sense :)

plt.hist(incomes, 50)

incomes = np.append(incomes, -10000000000)

plt.show()
