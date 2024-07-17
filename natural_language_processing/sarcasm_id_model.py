#%%
import json
import requests
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer # type:ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type:ignore

#%%
# processing and model params
vocab_size = 10000
embedding_dim = 16
max_length = 100
trunc_type='post'
padding_type='post'
oov_token = "<oov>"
training_size = 20000

# data load params
url = 'https://storage.googleapis.com/learning-datasets/sarcasm.json'
local_filename = 'files/sarcasm.json'

#%%
# request and write the data file
with requests.get(url) as r:
    with open(local_filename, 'w') as file:
        # have to decode bytes to string before write
        [file.write(i.decode('utf-8')) for i in r.iter_content()]        

#%%
# load training data
with open(local_filename, 'r') as file:
    datastore = json.load(file)

sentences, labels = [], []

for item in datastore:
    sentences.append(item['headline'])
    labels.append(item['is_sarcastic'])

#%%
# separation of data for training and testing
training_sentences = sentences[0:training_size]
testing_sentences = sentences[training_size:]
training_labels = np.array(labels[0:training_size])
testing_labels = np.array(labels[training_size:])
# some data have to use np.array because Tensorflow's format

#%%
# Tokenization (only training data)
tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
tokenizer.fit_on_texts(training_sentences)

word_index = tokenizer.word_index

# Sentences using their indexes instead words
training_sequences = tokenizer.texts_to_sequences(training_sentences)
training_padded = np.array(pad_sequences(training_sequences, maxlen=max_length,
                                         padding=padding_type, truncating=trunc_type))

testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
testing_padded = np.array(pad_sequences(testing_sequences, maxlen=max_length,
                                        padding=padding_type, truncating=trunc_type))

#%%
# callback to guarantee the best val_acc
# the final model tends to overfitting. +acc, and -val_acc.
from tensorflow.keras.callbacks import ModelCheckpoint # type:ignore
best_model_path = 'files/best_model.h5'
checkpointer = ModelCheckpoint(filepath=best_model_path, monitor='val_loss',
                               verbose=1, save_best_only=True) 

#%%
# model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

print(model.summary())

#%%
num_epochs = 100
history = model.fit(x=training_padded, y=training_labels, epochs=num_epochs,
                    validation_data=(testing_padded, testing_labels), verbose=1,
                    callbacks=checkpointer)

#%%
from tensorflow.keras.models import load_model # type:ignore

best_model = load_model(best_model_path)

#%%
def to_test_format(sentences):
    sequences = tokenizer.texts_to_sequences(sentences)
    padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type,
                           truncating=trunc_type)
    return padded

sentences = ['I have to wake up early tomorrow', 'game of thrones season finale showing this sunday night',
             'granny starting to fear spiders in the garden might be real']

print("Default model:\n", model.predict(to_test_format(sentences)))
print("Best acc_val model:\n", best_model.predict(to_test_format(sentences)))

# %%


