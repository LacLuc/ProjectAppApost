import itertools
import math

def gerar_combinacoes(elementos: list[int], tamanho: int) -> list[tuple[int]]:
    return list(itertools.combinations(elementos, tamanho))

def calcular_combinacoes(n: int, k: int) -> int:
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def range_number(n: int) -> list[int]:
    return [y + 1 for y in range(n)]

def valor_apostas(n: int, tipo: str) -> int:
    valores_loto = {15: 3, 16: 8, 17: 408, 18: 2448, 19: 11628, 20: 46512}
    valores_mega = {6: 5, 7: 35, 8: 140, 9: 420, 10: 1050, 11: 2310, 12: 4620, 
                    13: 8580, 14: 15015, 15: 25025, 16: 40040, 17: 64880, 
                    18: 92820, 19: 135660, 20: 193800}
    
    if tipo == "L":
        return valores_loto.get(n, 0)
    elif tipo == "M":
        return valores_mega.get(n, 0)
    return 0

def comb_apost() -> None:
    tipo = input("Loto, Mega: L/M: ").strip().upper()
    if tipo == 'L':
        x = 25
    elif tipo == 'M':
        x = 60
    else:
        print("Tipo inválido!")
        return
    
    elementos = range_number(x)
    tamanho = int(input("Tamanho - Loto 15 a 20, Mega 6 a 20: ").strip())

    combinacoes = gerar_combinacoes(elementos, tamanho)
    valor = valor_apostas(tamanho, tipo)
    valor_formatado = f"R${valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        
    resultado = calcular_combinacoes(len(elementos), tamanho)
    total = resultado * valor
    total_formatado = f"R${total:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

    print(f"Combinações de {tamanho} elementos de {min(elementos)} até {max(elementos)}: {resultado} Vlr_Aposta:{valor_formatado} Total:{total_formatado}")
    for indice, combinacao in enumerate(combinacoes, start=1):
        print(f"{str(indice).zfill(7)}: {combinacao}")

comb_apost()
