import pandas as pd

ecom = pd.read_csv("/home/gabriel-note/Documentos/mycodes/LAMIA/Material de aulas/Python-Data-Science-and-Machine-Learning-Bootcamp/2. Python para análise de dados/Pandas/Pandas Exercises/Ecommerce Purchases")

ecom.head() # 5 primeiras linhas do DataFrame

len(ecom.index) # número de linhas
len(ecom.columns) # número de colunas

round(ecom['Purchase Price'].mean(), 2) # Preço médio de compra

ecom['Purchase Price'].min() # Menor valor

ecom['Purchase Price'].max() # Maior valor

len(ecom[ecom['Language']=='en']) # número de pessoas que escolheram inglês como sua língua

len(ecom[ecom['Job']=='Lawyer']) # número de pessoas  que têm o cargo de advogado

ecom['AM or PM'].value_counts()['AM'] # número de pessoas que compraram no AM
ecom['AM or PM'].value_counts()['PM'] # número de pessoas que compraram no PM

ecom.groupby('Job')['Job'].value_counts().sort_values(ascending=0).head() # Cargos mais comuns em ordem decrescente

if ecom[ecom['Lot'] == '90 WT'].empty:
    "Ninguém comprou"
else:
    ecom[ecom['Lot'] == '90 WT']['Purchase Price'].iloc[0] # por quantos o lote 90 WT foi comprado

credit_card = ecom[ecom['Credit Card'] == 4926535242672853]

if credit_card.empty:
    "Ninguém possui esse cartão de crédito"
else:
    credit_card['Email'].iloc[0] # E-mail do portador do cartão de crédito


american_express_users = ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)]

len(american_express_users) # Número de pessoas que usam o American Express e Fizeram compras acima de U$ 95")

yy_CC_date = pd.DataFrame(ecom['CC Exp Date'].apply(lambda x: x[3:]))

len(ecom[yy_CC_date['CC Exp Date'] == '25']) # Número de cartões que vão expirar em 2025


def dominio(email): # Poderia ter usado o split()
    for i in range(0, len(email)):
        if email[i] == '@':
            return email[i:]

pd.DataFrame(ecom['Email'].apply(dominio)).value_counts().sort_values(ascending=False).head() # Provedores de email mais populares cadastrados

