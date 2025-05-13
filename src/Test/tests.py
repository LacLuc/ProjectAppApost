import random
from rich.progress import track
from time import sleep

def gera_jogos():
    numero_de_jogos = int(input('Digite a Qtde: '))
    log = input('Ativar log (s ou n): ')
    #jogos = [[] for _ in range(numero_de_jogos)]
    i = 1

    while i <= numero_de_jogos:
        lotofacil = lotofacil_generator()
        register = selectDados()
        if lotofacil in register:
            continue
        else:    
            #db.SaveFile.SeveDados(str(i).zfill(6), lotofacil)    
            SeveDados(str(i).zfill(6), lotofacil)
           
            if log == 's' or log == 'S':
                for t in track(range(10), print(str(i).zfill(6), lotofacil)):
                    sleep(0.1)    
            else:
                print(str(i).zfill(6), lotofacil)                 
            i += 1
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


def QtdeRegistros():
    register = selectDados()
    print('==>> Total de combinações 3268760 da Lotofácil!')
    print(f'==>> Qtde de Registro {len(register)}')
    print(f'==>> Falta gerar {3268760 - len(register)} combinações')


def SeveDados(ID, Ref1):
        try:
            with open(f'wdb_ProbAllArkivo.txt', 'a+') as file:      
                file.write(f"{Ref1} \n")
                file.seek(0)
        except ValueError:
                    print(f'Existe Um Erro')


def selectDados():
        try:
            with open(f'wdb_ProbAllArkivo.txt', 'r', encoding='utf-8') as file:
                content = file.readlines()
            return content
        except ValueError:
                        print(f'Existe Um Erro')


gera_jogos()