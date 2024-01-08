"""Resolução dos exercícios²"""

import pandas as pd

sal = pd.read_csv('pandas_exercises/files/Salaries.csv')

sal.head()

sal.info()

sal['BasePay'].mean() # BasePay médio

sal['OvertimePay'].max() # Maior valor do 'OvertimePay'

sal['JobTitle'][sal['EmployeeName'] == 'JOSEPH DRISCOLL'].to_string(index=False, dtype=False) # cargo do JOSEPH DRISCOLL
sal['TotalPayBenefits'][sal['EmployeeName'] == 'JOSEPH DRISCOLL'].to_string(index=False, dtype=False) # Salário do JOSEPH DRISCOLL

sal['EmployeeName'][sal['TotalPayBenefits'].idxmax()] # Nome da pessoa mais bem paga

sal.iloc[sal['TotalPayBenefits'].idxmin()] # Info da pessoa menos paga

group_year = sal[['Year', 'BasePay']].groupby('Year').mean()
group_year[(group_year.index >= 2011) & (group_year.index <= 2014)] # Média do Basepay(2011/2014)

len(sal['JobTitle'].value_counts())# Número de títulos de trabalho # poderia ter usado o nunique()

sal['JobTitle'].value_counts().head()# Cargos mais populares

# """Fiz desse jeito pois o tamanho do resultado da consulta com o 'value_counts == 1' não condizia com o tamanho do DataFrame original :)"""
def dupla_consulta (df, coluna1, coluna2, consulta1, consulta2): # poderia ter feito o somatório do dataframe booleano (True=1 e False=0)
    res = df[coluna1] == consulta1
    res = df[res]
    res = res[coluna2].value_counts()
    return res[res == consulta2]

len(dupla_consulta(sal, 'Year', 'JobTitle', 2013, 1)) # Titulos representados por apenas uma pessoa em 2013

bool = list(map(lambda str: 'CHIEF' in str.upper(), sal['JobTitle']))
len(sal[bool]['JobTitle']) # Número de pessoas que possuem a palavra Chefe em seu cargo
