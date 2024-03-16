from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.01)

plt.figure(1)
plt.plot(x, norm.pdf(x))
plt.title('Distribuição Gaussiana Balanceada (Assimetria = 0)')
plt.show()

plt.figure(2)
plt.plot(x, norm.pdf(x), label='Padrão')  # Distribuição padrão
plt.plot(x, norm.pdf(x, 1.0, 0.5), label='Personalizada') # Parâmetros: 1 -> média, 0.5 -> desvio padrão
plt.plot(x, norm.pdf(x, np.mean(x), np.std(x)), label='Baseada em x')  # Parâmetros baseados em x

plt.title('Múltiplas Funções em uma Única Figura')
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.legend()
plt.xlim([-5, 5])
plt.ylim([0, 1.0])

plt.show()

plt.xkcd() # LOL

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])
ax.set_ylim([-30, 10])

data = np.ones(100)
data[70:] -= np.arange(30)

plt.annotate(
    'THE DAY I REALIZED\nI COULD COOK BACON\nWHENEVER I WANTED',
    xy=(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(15, -10))

plt.plot(data)

plt.xlabel('time')
plt.ylabel('my overall health')

plt.show()
