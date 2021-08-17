import pandas as pd

#Criando um Dataframe - Estrutura de dados em linhas e colunas. No exemplo a coluna é  ('prince') e as linhas sao determinadas pela lista 'index' 

brent = pd.DataFrame({'price' : [63.8 , 55.7 , 32.5 , 18.4 , 29.4 , 40.3 , 43.2 , 44.7 , 40.9 , 40.2 , 42.7 , 50]} , index = ['Jan' , 'Fev' , 'Mar' , 'Abr' , 'Mai' , 'Jun' , 'Jul' , 'Ago' , 'Set' , 'Out' , 'Nov' , 'Dez'])

#print(brent)

#NomeDoDataFrame['Coluna']['indice que representa a linha] - retorna o valor localizado em determinada coluna e índice
#Se indice da linha é 0 (primeira linha) o valor da coluna 'delta' será o mesmo da coluna 'price'
#Caso contrário, ele vai devolver a diferença entre o valor de price e o anterior
#utilizando range para percorrer todas as linhas pelos índices

deltas = [brent['price'][i] if i == 0 else brent['price'][i] - brent['price'][i-1] for i in range (len(brent))]

#incluindo a lista de diferenças como uma coluna no dataframe
brent["deltas"] = deltas

#print(brent)

import waterfall_chart

#plotando o gráfico (eixo x , eixo y)
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["figure.figsize"] = (10,6)

waterfall_chart.plot(brent.index, brent['deltas']) 
plt.show()

