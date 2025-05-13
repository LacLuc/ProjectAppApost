def calcular_porcentagem_circular(posicao):
  """
  Calcula o peso de porcentagem para uma dada posição na tabela circular.
  Args:
    posicao: Um inteiro representando a posição na tabela (de 1 a 25).
  Returns:
    O peso de porcentagem correspondente à posição.
  """
  pesos = {
      1: 0.52, 2: 0.56, 3: 0.60, 4: 0.64, 5: 0.68, 6: 0.72, 7: 0.76, 8: 0.80, 9: 0.84, 10: 0.88,
      11: 0.92, 12: 0.96, 13: 1.00, 14: 0.96, 15: 0.92, 16: 0.88, 17: 0.84, 18: 0.80, 19: 0.76,
      20: 0.72, 21: 0.68, 22: 0.64, 23: 0.60, 24: 0.56, 25: 0.52
  }
  return pesos.get(posicao, "Posição inválida")

def preencher_tabela_circular(centro):
  """
  Preenche a tabela circular com números de 1 a 25, começando pelo centro.
  Args:
    centro: Um inteiro entre 1 e 25 que será colocado na posição 13 (centro).
  Returns:
    Um dicionário representando a tabela preenchida com números e seus pesos.
  """
  if not 1 <= centro <= 25:
    return "Número central inválido (deve estar entre 1 e 25)."

  tabela = {}
  numeros = list(range(1, 26))
  indice_centro = numeros.index(centro)

  # Preenche a partir da posição 13 até 25
  for i in range(13, 26):
    numero_atual = numeros[(indice_centro + (i - 13)) % 25]
    peso = calcular_porcentagem_circular(i)
    tabela[i] = {"numero": numero_atual, "peso": f"{peso:.2f}"}

  # Preenche da posição 1 até 12
  for i in range(1, 13):
    numero_atual = numeros[(indice_centro - (13 - i)) % 25]
    peso = calcular_porcentagem_circular(i)
    tabela[i] = {"numero": numero_atual, "peso": f"{peso:.2f}"}

  return tabela

# Exemplo de preenchimento com o número 25 no centro
tabela_preenchida_exemplo = preencher_tabela_circular(5)

# Imprimindo a tabela preenchida
for posicao, dados in sorted(tabela_preenchida_exemplo.items()):
  print(f"Posição {posicao:2d}: Número = {dados['numero']:2d}, Peso = {dados['peso']}")