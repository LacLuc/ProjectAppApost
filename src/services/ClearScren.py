import os

def cls():
    """
    Limpa a tela do terminal para Windows ou Unix.
    """
    sistema = os.name
    if sistema == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Para usar a função, basta chamar: