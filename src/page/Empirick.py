# Para criar um robô que valida a probabilidade de 70% de acertar 2 números em um range de 25
# números, precisamos entender o contexto probabilístico e desenvolver um algoritmo para simular
# ou calcular essa probabilidade. Vou assumir que você está se referindo a um sorteio onde 2 
# números são escolhidos aleatoriamente de um total de 25 números (como em um jogo de loteria ou
# bingo), e o robô deve verificar se a chance de acertar esses 2 números específicos atinge ou
# excede 70%. Como a probabilidade real de acertar 2 números em 25 é muito menor que 70%, 
# também considerarei a possibilidade de você estar pedindo um sistema que simule ou ajuste
# condições para alcançar essa probabilidade.

# Aqui está uma solução em Python que:

# 1. Calcula a probabilidade teórica de acertar 2 números em um range de 25.
# 2. Simula sorteios para validar empiricamente a probabilidade.
# 3. Verifica se a probabilidade de 70% é alcançável ou ajusta o contexto (se necessário).
# 4. Fornece um "robô" que realiza validações repetidas e retorna resultados.

### Código do Robô

import random
import itertools

def calcular_probabilidade_teorica():
    # Total de números: 25
    # Escolher 2 números
    total_combinacoes = len(list(itertools.combinations(range(1, 26), 2)))  # Combinações de 25 números, 2 a 2
    # Probabilidade de acertar 2 números específicos
    combinacoes_sucesso = 1  # Apenas 1 par específico é o desejado
    probabilidade = combinacoes_sucesso / total_combinacoes
    return probabilidade * 100  # Em porcentagem

def simular_sorteio(numeros_escolhidos, num_simulacoes=100000):
    acertos = 0
    for _ in range(num_simulacoes):
        # Sorteia 2 números de 1 a 25
        sorteio = random.sample(range(1, 26), 2)
        # Verifica se os números sorteados são exatamente os escolhidos
        if sorted(sorteio) == sorted(numeros_escolhidos):
            acertos += 1
    probabilidade_simulada = (acertos / num_simulacoes) * 100
    return probabilidade_simulada

def validar_probabilidade_70(numeros_escolhidos, num_simulacoes=100000):
    # Calcula probabilidade teórica
    prob_teorica = calcular_probabilidade_teorica()
    # Simula sorteios
    prob_simulada = simular_sorteio(numeros_escolhidos, num_simulacoes)
    
    print(f"Probabilidade teórica de acertar {numeros_escolhidos}: {prob_teorica:.4f}%")
    print(f"Probabilidade simulada ({num_simulacoes} simulações): {prob_simulada:.4f}%")
    
    # Verifica se a probabilidade é >= 70%
    if prob_simulada >= 70:
        print("A probabilidade simulada atinge ou excede 70%!")
    else:
        print("A probabilidade está abaixo de 70%.")
        # Calcula quantos números adicionais seriam necessários para alcançar ~70%
        print("Para alcançar 70%, seria necessário um contexto diferente (e.g., mais números sorteados ou range menor).")

# Exemplo de uso
numeros_escolhidos = [5, 10]  # Números escolhidos pelo usuário
print(f"Validando para os números {numeros_escolhidos}")
validar_probabilidade_70(numeros_escolhidos)


### Explicação do Código

# 1. **Cálculo Teórico**:
#    - O número total de combinações de 2 números em 25 é dado por \( C(25, 2) = \frac{25!}{2!(25-2)!} = 300 \).
#    - A probabilidade de acertar um par específico (e.g., [5, 10]) é \( \frac{1}{300} \approx 0,3333\% \), muito abaixo de 70%.

# 2. **Simulação**:
#    - O robô realiza `num_simulacoes` sorteios (padrão: 100.000) de 2 números entre 1 e 25.
#    - Verifica quantas vezes os números sorteados correspondem exatamente aos números escolhidos.
#    - Calcula a probabilidade empírica como \( \frac{\text{acertos}}{\text{simulações}} \times 100 \).

# 3. **Validação de 70%**:
#    - Compara a probabilidade simulada com o limiar de 70%.
#    - Como a probabilidade real é muito baixa, o robô informa que 70% não é alcançado e sugere que o 
#      contexto (e.g., mais números sorteados ou range menor) precisaria mudar.

# 4. **Flexibilidade**:
#    - O usuário pode alterar `numeros_escolhidos` (e.g., [5, 10]) e `num_simulacoes` para testar diferentes cenários.
#    - O código usa `random.sample` para garantir sorteios sem repetição e `itertools.combinations` para cálculos teóricos precisos.

### Exemplo de Saída

# Para `numeros_escolhidos = [5, 10]`:
