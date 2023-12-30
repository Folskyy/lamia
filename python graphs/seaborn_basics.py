import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid") # estilo do gráfico

plt.figure(1)

# planilha com informações diversos carros
df = pd.read_csv("http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv") 

gear_counts = df['# Gears'].value_counts() # conta o número de carros que possui cada câmbio
gear_counts.plot(kind='bar')
plt.show()


plt.figure(2)
plt.pie(gear_counts, labels=gear_counts.index)

df2 = df[['Cylinders', 'CityMPG', 'HwyMPG', 'CombMPG']]

plt.figure(3)
sns.pairplot(df2, hue='Cylinders', height=2.5);
plt.figure('scatter plot')
sns.scatterplot(x='# Gears', y='CombMPG', data=df)
plt.show()

plt.figure('implot')
sns.lmplot(x='# Gears', y='CombMPG', data=df)
plt.show()

plt.figure('jointplot')
sns.jointplot(x='# Gears', y='CombMPG', data=df) # nos da um histograma em cada eixo
plt.show()

plt.figure('boxplot')
sns.boxplot(x='# Gears', y='CombMPG', data=df)
plt.show()

plt.figure('1')
sns.swarmplot(x='# Gears', y='CombMPG', data=df)
plt.show()
