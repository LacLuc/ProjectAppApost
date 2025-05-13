#Gerar todas as 3.268.760 combinações da Lotofácil? 3268760
import random
from rich.progress import track
from time import sleep
import src.services.SelectFile as dba
import src.services.SaveFile as dbb
import ast

def gera_jogos():
    numero_de_jogos = int(input('Digite a Qtde: '))
    log = input('Ativar log (s ou n): ')
    #jogos = [[] for _ in range(numero_de_jogos)]
    i = 1    
    y = 0
    tb = []

    try:
        while i <= numero_de_jogos:
            #Criar uma função para poder digitar os numeros
            ASQ = input('deseja informa os numeros (s ou n): ')
            if ASQ == 'n' or ASQ == 'N':
                lotofacil = lotofacil_generator()
            else:
                for y in range(15):
                    QTDE = int(input(f'Digite o Nro{y+1}: '))
                    tb.append(QTDE)
                lotofacil = tb
                tb = []

            register = dba.SelectFile.selectDados()

            #função que valide a existencia do jogo...
            indices_encontrados = encontrar_lista(lotofacil, register)
            print(f'indices_encontrados: {indices_encontrados}-{lotofacil}') 

            if len(indices_encontrados) > 0:
                i += 1
                continue    
            else:    
                #db.SaveFile.SeveDados(str(i).zfill(6), lotofacil)    
                dbb.SaveFile.SeveDados(str(i).zfill(6), lotofacil)
            
                if log == 's' or log == 'S':
                    for t in track(range(10), print(str(i).zfill(6), lotofacil)):
                        sleep(0.1)    
                else:
                    print(str(i).zfill(6), lotofacil)                 
            i += 1
    except ValueError:
        print(f'Erro ao Executar {ValueError.args} o processo Query! ')
    QtdeRegistros()


def lotofacil_generator():
    resultado = []
    randow = random.Random()
    i = 0

    while i < 15:
        randow_number = randow.randint(1, 25)
        if randow_number in resultado:
            continue
        resultado.append(randow_number)
        i += 1
    resultado.sort()
    return resultado


def encontrar_lista(lista_procurar, listas):
    """
    Função que busca uma lista específica dentro de várias listas.

    Argumentos:
      lista_procurar (list): A lista a ser procurada.
      listas (list of lists): A lista de listas onde a busca será realizada.
    
    Retorna:
      list: Uma lista contendo os índices das listas onde a lista_procurar foi encontrada.
    """
    indices = []
    for i, lista in enumerate(listas):
      lista = lista.strip()
      lista = ast.literal_eval(lista)

      if lista_procurar == lista:
        indices.append(i)
    return indices


#lista_procurar = [1, 2, 3]
#listas = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9],[1, 2, 3]]




def QtdeRegistros():
    register = dba.SelectFile.selectDados()
    print('==>> Total de combinações 3268760 da Lotofácil!')
    print(f'==>> Qtde de Registro {len(register)}')
    print(f'==>> Falta gerar {3268760 - len(register)} combinações')


#gera_jogos()