
import pandas as pd
import numpy as np

colunas = []
linhas = []

#colunas = 'N1 N2 N3 N4 N5 N6 N7 N8 N9 N10 N11 N12 N13 N14 N15 N16 N17 N18 N19 N20 N21 N22 N23 N24 N25'.split()
def LoadColunas():
    n = int(input("Digite a Qty de Colunas: "))
    x = 1
    while x <= n:
        colunas.append(f'N{x}')
        x += 1
    return colunas

#linhas = 'Jogo1 Jogo2 Jogo3 Jogo4 Jogo5 Jogo6 Jogo7 Jogo8 Jogo9 Jogo10'.split()
def LoadLinhas():
    n = int(input("Digite a Qty de Linhas: "))
    y = 1
    while y <= n:
        linhas.append(f'Jogo{y}')
        y += 1
    return linhas


colunn = LoadColunas()
line = LoadLinhas()
dados = np.random.randint(0,2,len(line)*len(colunn)).reshape(len(line),len(colunn))
df = pd.DataFrame(data = dados, index = line, columns = colunn)
print(df)

