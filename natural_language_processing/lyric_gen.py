#%%
import requests
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences # type:ignore
from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional # type:ignore
from tensorflow.keras.preprocessing.text import Tokenizer # type:ignore
from tensorflow.keras.models import Sequential # type:ignore
from tensorflow.keras.optimizers import Adam # type:ignore

#%%
url = 'https://storage.googleapis.com/learning-datasets/irish-lyrics-eof.txt'
local_filename = 'files/irish-lyrocs-eof.txt'

with requests.get(url) as r:
    with open(local_filename, 'w') as file:
        file.write(b''.join([i for i in r.iter_content()]).decode('utf-8'))

# %%
tokenizer = Tokenizer()

data = open(local_filename).read()

corpus = data.lower().split('\n')

tokenizer.fit_on_texts(corpus)

total_words = len(tokenizer.word_index) + 1

print(tokenizer.word_index)
print(total_words)

#%%
input_sequences = []
for line in corpus:
    # retorna uma lista dentro de uma lista, por isso o [0]
	token_list = tokenizer.texts_to_sequences([line])[0]
	for i in range(1, len(token_list)):
		n_gram_sequence = token_list[:i+1]
		input_sequences.append(n_gram_sequence)

# pad sequences 
max_sequence_len = max([len(x) for x in input_sequences])
input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

# create predictors and label
# : pega todas as linhas, :-1 todas as colunas exceto a última
# : todas as linhas, -1 última coluna
xs, labels = input_sequences[:,:-1],input_sequences[:,-1]

# one-hot encode
ys = tf.keras.utils.to_categorical(labels, num_classes=total_words)
# %%
model = Sequential()
model.add(Embedding(total_words, 100, input_length=max_sequence_len-1))
model.add(Bidirectional(LSTM(150)))
model.add(Dense(total_words, activation='softmax'))
adam = Adam(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
print(model.summary())

#%%
#earlystop = EarlyStopping(monitor='val_loss', min_delta=0, patience=5, verbose=0, mode='auto')
history = model.fit(xs, ys, epochs=100, verbose=1)
#print model.summary()
print(model)

# %%
# seed_text = "I've got a bad feeling about this"
seed_text = "Knocking on heaven's"
next_words = 10

def to_test_format(seed_text, next_words):
	text = seed_text
	for _ in range(next_words):
		token_list = tokenizer.texts_to_sequences([text])[0]
		token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
		predicted = np.argmax(model.predict(token_list), axis=-1)
		output_word = ""
		for word, index in tokenizer.word_index.items():
			if index == predicted:
				output_word = word
				break
		text += " " + output_word
	return text

print(to_test_format(seed_text, next_words))

#%%