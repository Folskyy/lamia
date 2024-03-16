from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.01)

plt.figure(1) # a função em si cria uma tela vazia

plt.plot(x, norm.pdf(x)) # função para um gráfico de uma distribuição gaussiana
plt.title('distribuição gaussiana balanceada (Assimetria = 0)')
plt.show()

plt.figure(2) # múltuiplas funções em uma única figura

axes = plt.axes() # add um conjunto de eixos
axes.set_xlim([-3, 3]) # seta um limita para o eixo x
axes.set_ylim([0, 1]) # seta um limita para o eixo y
axes.set_xticks([-3, -2, -1, 0, 1, 2, 3]) # define os marcadores no eixo x
axes.set_yticks([0, 0.5, 1]) # define os marcadores no eixo y
axes.grid() # linhas de grade

# plt.xlim([-3, 3])
# plt.ylim([0, 1])

plt.plot(x, norm.pdf(x), 'r--')
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'g-.') # parametros: 1-> média, 0.5 -> desvio padrão
plt.plot(x, norm.pdf(x, np.mean(x), np.std(x)))

plt.xlabel('Possíveis valores') # rótulo do eixo x
plt.ylabel('Probabilidade') # rótulo do eixo y

plt.legend(['Normal', 'x(média=1 e var=0.5)', 'x(média e variância da array)']) # legenda

plt.savefig('output/distros_gauss.png') # salva o gráfico

plt.show() # plota o gráfico

plt.figure(3)# gráfico de pizza
values = [14190280, 8347693, 10744658, 13742209, 10141922]
colors = ['c', 'g', 'b', 'r', 'm']
explode = [0, 0.1, 0, 0, 0] # destaca a fatia
labels = ['O xote das Meninas', 'Numa sala de Reboco', 'Pagode Russo', 'A vida do Viajante (ft. gonzaguinha)', 'Asa Branca']

plt.pie(values, colors=colors, labels=labels, explode=explode) # função do gráfico de pizza
plt.title('Músicas mais ouvidas do liuz gonzaga recentemente no spotify')

# plt.bar(range(0,5), values, color= colors)
plt.show()

plt.figure(4)
values = [37435191, 32941308, 29210808, 23209616, 22619736]
labels = ['TOKYO', 'NOVA DELHI', 'XANGAI', 'DHAKA', 'SÃO PAULO']

plt.bar(labels, values, color= colors) # função do gráfico de barras
plt.title('Cidades mais povoadas do mundo')
plt.show()

plt.figure(5)
plt.scatter(np.random.randn(100), np.random.rand(100)) # função do gráfico de dispersão
plt.show()

plt.figure(6)
incomes = np.random.normal(27000, 15000, 10000)
plt.hist(incomes, 50) # função do histograma
plt.show() # as barras representam o numero de dados que estão nesse intervalo

plt.figure(7)
uniformSkewed = np.random.rand(100) * 100 - 40
high_outliers = np.random.rand(10) * 50 + 100
low_outliers = np.random.rand(10) * -50 - 100
data = np.concatenate((uniformSkewed, high_outliers, low_outliers)) # concatenar arrays ao longo de um eixo
plt.boxplot(data) # função do quartil
plt.show()