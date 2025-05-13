### Ajustando para Alcançar 70%

# A probabilidade de 70% é extremamente alta para acertar 2 números específicos em um range 
# de 25. Para alcançar algo próximo de 70%, seria necessário:

# - **Aumentar o número de números sorteados**: Por exemplo, se 10 números fossem sorteados
# em vez de 2, a chance de acertar 2 números específicos aumentaria.
# - **Reduzir o range**: Um range menor (e.g., 5 números) aumenta a probabilidade.
# - **Ajustar o critério de sucesso**: Considerar "acertar pelo menos 1 número" em vez de
# "exatamente 2 números".

# Se você quiser um robô que ajuste o sorteio para garantir uma probabilidade de ~70%, posso
# modificar o código. Por exemplo, calcular quantos números precisam ser sorteados para que a 
# chance de acertar 2 específicos seja próxima de 70%. Um cálculo hipergeométrico pode 
# determinar isso:

# - Probabilidade de acertar 2 números em um sorteio de \( k \) números:
#   \[
#   P = \frac{C(2, 2) \cdot C(23, k-2)}{C(25, k)}
#   \]
# - Resolvendo para \( P \approx 0,7 \), podemos estimar \( k \).

# ### Código Ajustado (Opcional)

# Se você quiser calcular o número de sorteios necessário para ~70%:


from scipy.stats import hypergeom

def encontrar_numero_sorteios_para_70():
    N = 25  # Total de números
    n = 2   # Números desejados
    for k in range(2, 26):  # Testa diferentes quantidades de números sorteados
        prob = hypergeom.cdf(2, N, n, k) - hypergeom.cdf(1, N, n, k)  # P(exatamente 2 acertos)
        if prob >= 0.7:
            print(f"Para ~70% de chance, sorteie {k} números. Probabilidade: {prob*100:.2f}%")
            break
    else:
        print("Não é possível alcançar 70% mesmo sorteando todos os 25 números.")

# Chama a função
encontrar_numero_sorteios_para_70()


### Resposta Final

# O robô acima calcula e simula a probabilidade de acertar 2 números em um range de 25, mas a 
# probabilidade real é ~0,33%, muito abaixo de 70%. Para atingir 70%, seria necessário mudar o 
# contexto (e.g., sortear mais números). Se você quiser que o robô ajuste o sorteio ou simule um 
# cenário específico (e.g., sortear 10 números), por favor, уточните. Caso contrário, o código 
# fornecido é um robô funcional que valida a probabilidade e explica por que 70% não é alcançado
# no cenário padrão.