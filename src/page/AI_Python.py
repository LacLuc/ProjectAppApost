# Criando um modelo de aprendizado de máquina para combinações numéricas de 1 a 25
# A criação de um modelo de aprendizado de máquina para combinações numéricas de 1 a 25
# pode ser abordada de diversas formas, dependendo do objetivo específico. Vamos explorar 
# algumas possibilidades:
# 1. Previsão de combinações vencedoras na loteria
# Se o objetivo for prever combinações vencedoras na loteria, é importante entender que não
# existe um modelo de aprendizado de máquina capaz de garantir a vitória. Os resultados da 
# loteria são aleatórios e independentes, o que significa que não há padrões a serem aprendidos.
# No entanto, é possível utilizar aprendizado de máquina para analisar dados históricos de 
# sorteios e identificar tendências, como os números que são sorteados com mais frequência 
# ou as combinações que apareceram com mais frequência ao longo do tempo. Essa análise pode 
# fornecer insights interessantes, mas não garante a previsão de resultados futuros.
# 2. Geração de combinações com base em preferências
# Se o objetivo for gerar combinações numéricas com base em preferências pessoais, como 
# números da sorte ou datas de aniversário, é possível criar um modelo de aprendizado de 
# máquina que aprenda essas preferências e gere combinações personalizadas.
# Para isso, seria necessário coletar dados sobre as combinações preferidas do usuário e 
# utilizar algoritmos de aprendizado de máquina para identificar padrões e gerar novas 
# combinações que sigam essas preferências.
# 3. Classificação de combinações
# Se o objetivo for classificar combinações numéricas com base em critérios específicos, 
# como a soma dos números ou a presença de determinados números, é possível criar um modelo 
# de aprendizado de máquina que aprenda esses critérios e classifique novas combinações automaticamente.
# Para isso, seria necessário definir os critérios de classificação e fornecer um conjunto 
# de dados de treinamento com combinações numéricas e suas respectivas classes. Em seguida, 
# seria possível utilizar algoritmos de aprendizado de máquina para treinar o modelo e classificá-lo.
# Exemplo prático: previsão de números pares e ímpares
# Vamos criar um exemplo prático de como criar um modelo de aprendizado de máquina para 
# prever se uma combinação numérica de 5 dígitos (de 1 a 25) terá mais números pares ou ímpares.
# 1. Coleta de dados
# Geramos um conjunto de dados com 1000 combinações numéricas aleatórias de 5 dígitos (de 1 a 25) e 
# rotulamos cada combinação com "par" ou "ímpar" com base na contagem de números pares e ímpares.
# 2. Treinamento do modelo
# Utilizamos o algoritmo de aprendizado de máquina "Random Forest" para treinar um modelo capaz de 
# classificar novas combinações numéricas.
# 3. Avaliação do modelo
# Avaliamos a precisão do modelo utilizando um conjunto de dados de teste e verificamos se ele é 
# capaz de classificar corretamente novas combinações numéricas.
# 4. Utilização do modelo
# Utilizamos o modelo treinado para classificar novas combinações numéricas e obter a previsão de "par" ou "ímpar".
# Este é apenas um exemplo simples de como criar um modelo de aprendizado de máquina para 
# combinações numéricas. É importante lembrar que a escolha do algoritmo, a coleta de dados e o 
# objetivo do modelo podem variar dependendo do problema específico.
# Se você tiver alguma dúvida ou precisar de ajuda para criar um modelo específico, não hesite em perguntar.

from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import random
import numpy as np

#Deep Learning contínuo
#Criando um modelo de aprendizado profundo (Deep Learning) em 
# Python para combinações numéricas de 1 a 25 com capacidade de aprendizado contínuo
def gerar_combinacaoOne():
  return [random.randint(1, 25) for _ in range(15)]

def classificar_combinacaoOne(combinacao):
  pares = sum(1 for num in combinacao if num % 2 == 0)
  impares = 15 - pares
  return 1 if pares > impares else 0 # 1 para "par", 0 para "ímpar"

dados = []
for _ in range(1000):
  combinacao = gerar_combinacaoOne()
  classe = classificar_combinacaoOne(combinacao)
  dados.append((combinacao, classe))

X = np.array([combinacao for combinacao, classe in dados])
y = np.array([classe for combinacao, classe in dados])

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = Sequential([
    Dense(128, activation='relu', input_shape=(15,)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid') # Saída binária (0 ou 1)
])

modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

modelo.fit(X_treino, y_treino, epochs=10, batch_size=32)

y_pred = (modelo.predict(X_teste) > 0.5).astype(int) # Converter probabilidades em classes
precisão = accuracy_score(y_teste, y_pred)
print(f"Precisão do modelo: {precisão}")

#Para permitir que o modelo continue aprendendo com novos dados, 
#podemos adicionar uma função que recebe novos dados e os 
#utiliza para treinar o modelo por mais algumas épocas:
def continuar_treinamentoOne(novos_dados, novas_classes, epochs=5):
  X_novos = np.array(novos_dados)
  y_novos = np.array(novas_classes)
  modelo.fit(X_novos, y_novos, epochs=epochs, batch_size=32)

nova_combinacao = gerar_combinacaoOne()
probabilidade = modelo.predict(np.array([nova_combinacao]))[0][0]
classe_prevista = "par" if probabilidade > 0.5 else "ímpar"
nova_combinacao.sort()
print(f"Combinação: {nova_combinacao}")
print(f"Probabilidade de ser 'par': {probabilidade}")
print(f"Classe prevista: {classe_prevista}")

# Explicação do código:
# Importação das bibliotecas: Importa as bibliotecas necessárias para gerar dados aleatórios, 
# criar o modelo de aprendizado profundo, dividir os dados em treino e teste e avaliar o modelo.
# Geração do conjunto de dados: Define funções para gerar combinações numéricas aleatórias de 15 dígitos e 
# classificá-las como "par" ou "ímpar" (1 ou 0). Em seguida, gera um conjunto de dados com 1000 combinações e suas respectivas classes.
# Preparação dos dados: Converte os dados para o formato numpy array e divide-os em conjuntos de treino e teste.
# Criação e treinamento do modelo: Cria um modelo de rede neural profunda com camadas densas e função de ativação ReLU. 
# Utiliza a função de perda "binary_crossentropy" e o otimizador "adam".
# Avaliação do modelo: Avalia a precisão do modelo utilizando os dados de teste.
# Capacidade de aprendizado contínuo: Define uma função que recebe novos dados e classes e treina o modelo por mais algumas épocas.
# Utilização do modelo: Gera uma nova combinação numérica, utiliza o modelo treinado para prever sua classe e imprime a probabilidade de ser "par".
# Observações:
# Este é um exemplo básico de como criar um modelo de aprendizado profundo para combinações numéricas com capacidade de aprendizado contínuo.
# A arquitetura do modelo, os parâmetros de treinamento e a quantidade de dados podem ser ajustados para melhorar a precisão e o desempenho.
# A capacidade de aprendizado contínuo permite que o modelo se adapte a novos dados e melhore sua performance ao longo do tempo.


# Criando um modelo de aprendizado profundo (Deep Learning) em 
# Python para combinações numéricas de 1 a 25 com 
# capacidade de aprendizado contínuo e parâmetros informáveis

# # 1. Importação das bibliotecas necessárias:
# import random
# import numpy as np
# from tensorflow import keras
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score

# 2. Geração do conjunto de dados com parâmetros informáveis:
def gerar_combinacao(num_digitos=15, limite_superior=25):
  return [random.randint(1, limite_superior) for _ in range(num_digitos)]

def classificar_combinacao(combinacao):
  pares = sum(1 for num in combinacao if num % 2 == 0)
  impares = len(combinacao) - pares
  return 1 if pares > impares else 0 # 1 para "par", 0 para "ímpar"

dados = []
for _ in range(1000):
  combinacao = gerar_combinacao()
  classe = classificar_combinacao(combinacao)
  dados.append((combinacao, classe))


# 3. Preparação dos dados para o modelo:
X = np.array([combinacao for combinacao, classe in dados])
y = np.array([classe for combinacao, classe in dados])

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)


# 4. Criação e treinamento do modelo com parâmetros informáveis:
def criar_modelo(input_dim, num_camadas=2, unidades_por_camada=64, taxa_aprendizagem=0.001):
  modelo = Sequential()
  modelo.add(Dense(unidades_por_camada, activation='relu', input_shape=(input_dim,)))
  for _ in range(num_camadas - 1):
    modelo.add(Dense(unidades_por_camada, activation='relu'))
  modelo.add(Dense(1, activation='sigmoid')) # Saída binária (0 ou 1)

  otimizador = keras.optimizers.Adam(learning_rate=taxa_aprendizagem)
  modelo.compile(optimizer=otimizador, loss='binary_crossentropy', metrics=['accuracy'])
  return modelo

input_dim = X_treino.shape[1]
modelo = criar_modelo(input_dim)

modelo.fit(X_treino, y_treino, epochs=10, batch_size=32)


# 5. Avaliação do modelo:
y_pred = (modelo.predict(X_teste) > 0.5).astype(int) # Converter probabilidades em classes
precisão = accuracy_score(y_teste, y_pred)
print(f"Precisão do modelo: {precisão}")


# 6. Capacidade de aprendizado contínuo com novos parâmetros:
def continuar_treinamento(novos_dados, novas_classes, epochs=5, **kwargs):
  X_novos = np.array(novos_dados)
  y_novos = np.array(novas_classes)

  # Ajustar parâmetros do modelo, se fornecidos
  for chave, valor in kwargs.items():
    if hasattr(modelo, chave):
      setattr(modelo, chave, valor)

  modelo.fit(X_novos, y_novos, epochs=epochs, batch_size=32)


# 7. Utilização do modelo com novos parâmetros:
nova_combinacao = gerar_combinacao()
probabilidade = modelo.predict(np.array([nova_combinacao]))[0][0]
classe_prevista = "par" if probabilidade > 0.5 else "ímpar"
print(f"Combinação: {nova_combinacao}")
print(f"Probabilidade de ser 'par': {probabilidade}")
print(f"Classe prevista: {classe_prevista}")

# Informar novos parâmetros para o modelo
novos_dados = [gerar_combinacao() for _ in range(100)]
novas_classes = [classificar_combinacao(combinacao) for combinacao in novos_dados]
continuar_treinamento(novos_dados, novas_classes, epochs=5, num_camadas=3, unidades_por_camada=128)


# Explicação do código:
# Importação das bibliotecas: Importa as bibliotecas necessárias para gerar dados aleatórios, criar o modelo de aprendizado profundo, dividir os dados em treino e teste e avaliar o modelo.
# Geração do conjunto de dados com parâmetros informáveis: As funções gerar_combinacao e classificar_combinacao agora aceitam parâmetros opcionais num_digitos e limite_superior para controlar o tamanho das combinações e o limite superior dos números.
# Preparação dos dados: Converte os dados para o formato numpy array e divide-os em conjuntos de treino e teste.
# Criação e treinamento do modelo com parâmetros informáveis: A função criar_modelo agora aceita parâmetros opcionais num_camadas, unidades_por_camada e taxa_aprendizagem para personalizar a arquitetura do modelo e o otimizador.
# Avaliação do modelo: Avalia a precisão do modelo utilizando os dados de teste.
# Capacidade de aprendizado contínuo com novos parâmetros: A função continuar_treinamento agora aceita argumentos nomeados (**kwargs) que podem ser usados para ajustar os parâmetros do modelo durante o treinamento contínuo.
# Utilização do modelo com novos parâmetros: Demonstra como usar o modelo e como informar novos parâmetros durante o treinamento contínuo.
# Observações:
# Este exemplo demonstra como criar um modelo de aprendizado profundo com capacidade de aprendizado contínuo e parâmetros informáveis.
# A arquitetura do modelo, os parâmetros de treinamento e a quantidade de dados podem ser ajustados para melhorar a precisão e o desempenho.
# A capacidade de aprendizado contínuo permite que o modelo se adapte a novos dados e melhore sua performance ao longo do tempo.
# A possibilidade de informar novos parâmetros oferece flexibilidade para ajustar o modelo a diferentes cenários e necessidades.
# Lembre-se que este modelo específico foi projetado para classificar combinações numéricas com base na contagem de números pares e ímpares. Se você tiver um objetivo diferente, como prever resultados de loteria ou gerar combinações com base em preferências, será necessário adaptar o código e os dados de acordo.
# Se precisar de ajuda para adaptar o código para outro objetivo ou tiver alguma dúvida, me diga!
