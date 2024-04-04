from tensorflow.keras.preprocessing.text import Tokenizer # Objeto para indexar cada palavra # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # Ajuste do tamanho das sequencias # type: ignore

#%%
# simples amostra de palavras
sentences = [
    "I like eggs and ham.",
    "I love chocolate and bunnies.",
    "I hate onions."
]
MAX_VOCAB_SIZE = 20000
# objeto Tokenizer permite transformar palavras em sequências numéricas
# num_words = x -> somente as x palavras mais recorrentes no treinamento serão consideradas
tokenizer = Tokenizer(num_words=MAX_VOCAB_SIZE)

# método para a construção do vocábulário
tokenizer.fit_on_texts(sentences)
# conversão para sequencias numericas
sequences = tokenizer.texts_to_sequences(sentences)
print(sequences)

#%%
# palavras e seus respectivos indices
tokenizer.word_index

#%%
# parametros defaults
data = pad_sequences(sequences)
print(data)

#%%
# restringindo um tamanho para cada sequencia
MAX_SEQUENCE_LENGTH = 5
data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
print(data)

#%%
# padding='post' -> O padding adiciona os zeros no final da lista (à direita).
# É inserido no começo por default
data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH, padding='post')
print(data)

#%%
# Aumentando o limite de tamanho para as sequencias (Zeros à esquerda se o tamanho da lista for <= maxlen)
data = pad_sequences(sequences, maxlen=6)
print(data)

#%%
# Caso a lista seja maior que o limite, os valores iniciais da lista são ocultados para encaixar.
# já que essa estrutura dá mais importância às palavras finais de uma frase
data = pad_sequences(sequences, maxlen=4)
print(data)

#%%
data = pad_sequences(sequences, maxlen=4, truncating='post')
print(data)
