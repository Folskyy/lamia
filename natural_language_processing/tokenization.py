#%%
from tensorflow.keras.preprocessing.text import Tokenizer # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore

#%%
sentences = ['I love my dog',
             'I love my cat',
             'I love my dog!',
             'Do you think my dog is amazing?'
            ]

#%%
# tokenization: transforma as palavras para um formato que o PC consiga processar
# num_words -> N palavras mais recorrentes serão consideradas
# oov_token -> Adiciona um token padrão para palavras não contidas no dicionário
tokenizer = Tokenizer(num_words=100, oov_token='<oov>')
tokenizer.fit_on_texts(sentences)
# dicionário com as palavras e seus respectivos indices
word_index = tokenizer.word_index

# %%
# transforma as palavras das sentenças em índices
# senteças de índices
sequences = tokenizer.texts_to_sequences(sentences)
for i, sentence in enumerate(sequences):
    if i != 0:
        print(f"\nSentence number {i}: ")
    else:
        print(f"Sentence number {i}: ")
                
    [print(word, end=' ') for word in sentence]

# Recebe o tamanho da sentença mais longa.
max_len = [len(sent) for sent in sequences]
max_len = max(max_len)
#%%
print("Word : Index")
[print(f"{word} : {word_index[word]}") for word in word_index]

# %%
# padding ajusta para que as sentenças possuam o mesmo tamanho
# para isso, comumente é adicionado zeros à esquerda da sentença
padded = pad_sequences(sequences, maxlen=max_len)

[print(sentence) for sentence in padded]
# %%
test_data = ['I really love my dog',
             'my dog loves my mantee'
            ]

test_seq = tokenizer.texts_to_sequences(test_data)
print(test_seq)

#%%
padded = pad_sequences(test_seq, maxlen=10)
print("\nPadded Test Sequence: ")
print(padded)

# %%
