#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from tensorflow.keras.preprocessing.text import Tokenizer # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
from tensorflow.keras.layers import Dense, Input, GlobalMaxPooling1D # type: ignore
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Embedding # type: ignore
from tensorflow.keras.models import Model # type: ignore
#%%
# Unfortunately this URL doesn't work directly with pd.read_csv
# https://lazyprogrammer.me/course_files/spam.csv

#%%
# leitura dos dados
df = pd.read_csv('files/spam.csv', encoding='ISO-8859-1')
df.head()

#%%
# exclusão de colunas desnecessárias para o treinamento
df = df.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
df.head()

#%%
# alteração do nome das colunas
df.columns = ['labels', 'data']
df.head()

#%%
# labels binárias
df['b_labels'] = df['labels'].map({'ham': 0, 'spam': 1})
Y = df['b_labels'].values

#%%
# split up the data
df_train, df_test, Ytrain, Ytest = train_test_split(df['data'], Y, test_size=0.33)

#%%
# Convert sentences to sequences
MAX_VOCAB_SIZE = 20000
tokenizer = Tokenizer(num_words=MAX_VOCAB_SIZE) # criação do objeto Tokenizer
tokenizer.fit_on_texts(df_train) # construção do índice de palavras com base na frequencia
sequences_train = tokenizer.texts_to_sequences(df_train)
sequences_test = tokenizer.texts_to_sequences(df_test)

#%%
# get word -> integer mapping
word2idx = tokenizer.word_index # dicionário com as palavras e seus respectivos indices
V = len(word2idx)
print('Found %s unique tokens.' % V)


#%%
# adição do padding no tensor de treinamento
data_train = pad_sequences(sequences_train)
print('Shape of data train tensor:', data_train.shape)

#%%
# get sequence length
T = data_train.shape[1]

#%%
# adição do padding no tensor de teste
data_test = pad_sequences(sequences_test, maxlen=T)
print('Shape of data test tensor:', data_test.shape)

#%%
# Create the model

# n° de dimensões do embedding
D = 20

# Note: we actually want to the size of the embedding to (V + 1) x D,
# because the first index starts from 1 and not 0.
# Thus, if the final index of the embedding matrix is V,
# then it actually must have size V + 1.

i = Input(shape=(T,))
x = Embedding(V + 1, D)(i)
x = Conv1D(32, 3, activation='relu')(x)
x = MaxPooling1D(3)(x)
x = Conv1D(64, 3, activation='relu')(x)
x = MaxPooling1D(3)(x)
x = Conv1D(128, 3, activation='relu')(x)
x = GlobalMaxPooling1D()(x)
x = Dense(1, activation='sigmoid')(x)

model = Model(i, x)

#%%
# Compile and fit
model.compile(
  loss='binary_crossentropy',
  optimizer='adam',
  metrics=['accuracy']
)
#%%
r = model.fit(data_train, Ytrain, epochs=5, validation_data=(data_test, Ytest))

#%%
# Plot loss per iteration
import matplotlib.pyplot as plt
plt.plot(r.history['loss'], label='loss')
plt.plot(r.history['val_loss'], label='val_loss')
plt.legend()

#%%
# Plot accuracy per iteration
plt.plot(r.history['accuracy'], label='acc')
plt.plot(r.history['val_accuracy'], label='val_acc')
plt.legend()