import pandas as pd

base = pd.read_csv('/home/gabriel/Documentos/lamia/deep_learning/regression/autos.csv', encoding='ISO-8859-1')

# valores inconsistentes
base = base.drop('dateCrawled', axis=1)
base = base.drop('dateCreated', axis=1)
base = base.drop('nrOfPictures', axis=1)
base = base.drop('postalCode', axis=1)
base = base.drop('lastSeen', axis=1)

base['name'].value_counts()
base = base.drop('name', axis=1)
base['seller'].value_counts()
base = base.drop('seller', axis=1)
base['offerType'].value_counts()
base = base.drop('offerType', axis=1)

i1 = base.loc[base.price <= 10]
base = base[base.price > 10]
i2 = base.loc[base.price > 350000]
base = base[base.price < 350000]

# valores faltantes
base = base.dropna()

#label encoder
previsores = base.iloc[:, 1:13].values
preco_real = base.iloc[:, 0].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
# transformação de atributos categóricos para numéricos
encoder1 = LabelEncoder()
previsores[:, 0] = encoder1.fit_transform(previsores[:, 0])
previsores[:, 1] = encoder1.fit_transform(previsores[:, 1])
previsores[:, 3] = encoder1.fit_transform(previsores[:, 3])
previsores[:, 5] = encoder1.fit_transform(previsores[:, 5])
previsores[:, 8] = encoder1.fit_transform(previsores[:, 8])
previsores[:, 9] = encoder1.fit_transform(previsores[:, 9])
previsores[:, 10] = encoder1.fit_transform(previsores[:, 10])

encoder2 = ColumnTransformer(transformers=[("OneHot", OneHotEncoder(), [0,1,3,5,8,9,10])],remainder='passthrough')
previsores = encoder2.fit_transform(previsores).toarray()

from keras.models import Sequential
from keras.layers import Dense
# estruturando a rede neural
regressor = Sequential()
regressor.add(Dense(units=157, activation='relu', input_dim=314))
regressor.add(Dense(units=157, activation='relu'))
regressor.add(Dense(units=1, activation='linear')) # função de ativação que não altera a saída

regressor.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])

regressor.fit(previsores, preco_real, batch_size=300, epochs=100)

previsoes = regressor.predict(previsores)

