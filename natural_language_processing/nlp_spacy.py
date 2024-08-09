#%%
import spacy
import spacy.matcher

#%%
# SMall model
# nlp = spacy.load('en_core_web_sm')

# MeDium model
nlp = spacy.load('en_core_web_md')

#%%
text_path = 'files/wiki_us.txt'
with open(text_path, 'r') as f:
    text = f.read()

doc = nlp(text)

# %%
print("---8 primeiros elementos---")
print("Leitura simples: ")
# cada char é um elemento
[print(i) for i in text[:8]]

print("\nLeitura simples com split: ")
# cada elemento é separado por espaço
read_split = [print(i) for i in text.split()[:8]]

print("\nLeitura com spacy: ")
# cada palavra e pontuação é contado como elemento
spacy_token = [print(token) for token in doc[:8]]

# SBD (Sentence Boundary Detection)
# cada sentença é um elemento
# doc.sents é um gerador, por isso deve ser convertido para lista
print("8 primeiras sentenças")
[print(sent) for sent in list(doc.sents)[:8]]

# %%
token1 = list(doc.sents)[0][2]
print(token1)

# %%
# token attributes

# conteúdo textual
print(token1.text)

# o 'pai sintático' do token
print(token1.head)

# token 'da família' mais a esquerda
print(token1.left_edge)

# token 'da família' mais a direita
print(token1.right_edge)

# retorna o número (representador numérico) do tipo de entidade do token
print(token1.ent_type)
# retorna o tipo de entidade do token
print(token1.ent_type_)

# IOB
# I: Inside an entity
# O: Outside an entity
# B: Begins an entity
print(token1.ent_iob_)
# IOB number
print(token1.ent_iob)

# forma base do token
print(token1.lemma_)

# análise morfológica do token
print(token1.morph)

# classe gramatical
print(token1.pos_)

# dependencia gramatical
print(token1.dep_)

# idioma
print(token1.lang_)

# %%
text2 = "I hate non green frogs."
doc2 = nlp(text2)

for token in doc2:
    print(token.text, token.pos_, token.dep_)

# %%
# Visualizar dependencias do texto
from spacy import displacy

displacy.render(doc2, style='dep')

# %%
# visualização dos tipos das entidades identificadas
displacy.render(doc, style='ent')

# %%
######################################################################
import numpy as np
# VETOR DE PALAVRAS
# não funciona com o small model
your_word = 'Local'

# palavras parecidas com your_word usando o vetor de palavras
ms = nlp.vocab.vectors.most_similar(
    np.asarray([nlp.vocab.vectors[nlp.vocab.strings[your_word]]]), n=10)
words = [nlp.vocab.strings[w] for w in ms[0][0]]
distances = ms[2]
print("words like 'local':\n", words)

# %%
# similaridade entre textos
doc3 = nlp("I have to drink more water")
doc4 = nlp("She can do this all day")
doc5 = nlp("I am dehydrated")

# quoeficiente de semelhança entre os vetores resultantes dos textos
print(doc3, '<->', doc4, doc3.similarity(doc4))
print(doc3, '<->', doc5, doc3.similarity(doc5))

# %%
# Pipeline basicamente é um conjunto de ações efetuadas em um conjunto de dados
# Por default, o spacy.load() possui muitos componentes, o que pode resultar em um maior tempo de processamento
# Cria um modelo sem pipes (um objeto de linguagem 'lang' vazio):
nlp2 = spacy.blank('en')
# pipe que fragmenta o texto em frases
nlp2.add_pipe('sentencizer')
print("en_core_md pipeline:\n", nlp.analyze_pipes())
print("blank + sentencizer pipeline:\n", nlp2.analyze_pipes())

# nlp2.add_pipe('entity_ruler')
# nlp2.analyze_pipes()
# %%
nlp = spacy.load('en_core_web_sm')

text = "West Chestertenfieldville was referenced in Mr. Deeds."

# parametro before para alterar a 'ordem de prioridade' da categorização do token
ruler = nlp.add_pipe('entity_ruler', before='ner')
# padrão para uma regra
patterns = [
    {'label': 'GPE', 'pattern': 'West Chestertenfieldville'}
]
# adiciona regra ao pipe específicado
ruler.add_patterns(patterns)

#%%
with open('files/wiki_mlk.txt') as f:
    text = f.read()
#%%
nlp = spacy.load("en_core_web_sm")
matcher = spacy.matcher.Matcher(nlp.vocab)

# padrão que busca substantivos. OP +: diz para retornar todos os tokens que se repetem mais de uma vez
pattern = [{"POS": "PROPN", "OP": "+"}]

# o greedy=LONGEST permite que evite sobreposições de matches e retorne o match mais longo (que inclui todos os tokens encontrados)
matcher.add('PROPER_NOUNS', [pattern], greedy="LONGEST")

doc = nlp(text)
matches = matcher(doc)

#%%
# matches encontrados
for match in matches[:10]:
    print(match, doc[match[1]:match[2]])

# %%
# nlp = spacy.load('en_core_web_sm')
import json

with open('files/alice.json') as f:
    data = json.load(f)

text = data[0][2][0]
print(text)
text = text.replace("`", "'")
print(text)

# %%
# Matcher

nlp = spacy.load("en_core_web_sm")
matcher = spacy.matcher.Matcher(nlp.vocab)

doc = nlp(text)

pattern = [
    {'ORTH': "'"},
    {'IS_ALPHA': True, "OP": "*"},
    {'IS_PUNCT': True, "OP": "*"},
    {'IS_SPACE': True, "OP": "*"},
    {'ORTH': "'"}
]
matcher.add("PROPER NOUNS", [pattern], greedy='LONGEST')
matches = matcher(doc)

# %%
for match in matches[:10]:
    print(match, doc[match[1]:match[2]])

# %%
# Custom components
from spacy.language import Language

#%%
text = "Britain is a place. Mary is a doctor."
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

#%%
for ent in doc.ents:
    print(ent.text, ent.label_)

# %%
# Componente personalizada
@Language.component("remove_gpe")
def remove_gpe(doc):
    original_ents = list(doc.ents)
    for ent in doc.ents:
        if ent.label_ == 'GPE':
            original_ents.remove(ent)
    doc.ents = original_ents
    return doc

#%%
print("Antes de adicionar o custom component:\n", nlp.analyze_pipes())
nlp.add_pipe("remove_gpe")
print("Depois de adicionar o custom component:\n", nlp.analyze_pipes())

#%%
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)

# %%
