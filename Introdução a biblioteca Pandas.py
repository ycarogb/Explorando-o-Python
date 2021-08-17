from numpy.core.numeric import NaN
import pandas as pd

#abrindo um arquivo csv

DataFrame = pd.read_csv("C:/Users/Cliente/OneDrive/LABIKS/Estudos e Pesquisas/Gestão e Compartilhamento de Dados/Github/Annual Report/2020/Teste_Base de Dados.csv",  sep = ";", encoding = 'ISO-8859-1')


# CONHECENDO SEUS DADOS 
# o programa devolve um resumo do seu banco de dados com o conteúdo das cinco primeiras linhas
print(DataFrame.head())

#este programa devolve a quantidade de linhas e colunas do seu banco de dados ('linhas' , 'colunas')
print(DataFrame.shape)

#informações sobre o dataframe
print(DataFrame.info())

#ESTATÍSTICAS DESCRITIVAS
#Retorna medidas de tendência central
#a função considera apenas elementos "calculáveis" (números)

print(DataFrame.describe())

#deletando colunas

del DataFrame ['Source']

# #deletando uma linha

for x in range (2 , 5):
    DataFrame.drop(90 + x , axis= 0 , inplace= True)

#para eliminar as linhas vazias tambem pode usar a função dataframe.dropna()

print(DataFrame.sort_index())

