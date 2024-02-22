import re
from collections import Counter

def contar_palavras(arquivo):
    """Retorna uma lista das palavras individualmente (todas as palavras sem repeti-lás)"""
    with open(arquivo, 'r') as f:
        conteudo = f.read()
        palavras = re.findall(r'\b\w+\b', conteudo)
        return palavras

def ranquear_palavras(arquivo):
    """Com a lista da função contar_palavras(), é contado a recorrência de cada palavra da lista no arquivo"""
    palavras = contar_palavras(arquivo)
    contagem_palavras = Counter(palavras)
    palavras_ranqueadas = contagem_palavras.most_common()

    return palavras_ranqueadas

arquivo = 'output/job_logs.md'
resultado = ranquear_palavras(arquivo)

with open('output/rank_words.md', 'w') as f:
    for palavra, contagem in resultado:
        f.write(f"# {palavra}: # *{contagem} vezes.*\n")
