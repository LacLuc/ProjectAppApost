#qpy:console
import random as rd
from time import sleep
import src.services.NewID as NewID

def newApostMega(nu, max, mod): 
    try:
        Status = 'S'
        while Status == 'S' or Status == 's':
            Status = input('Deseja Continuar - Mega Six... (S ou N): ')
            if Status == "S" or Status == 's':
                createApostQ(nu, max, mod)
            elif Status == "N" or Status == 'n':    
                break
            else:
                print("Você deve informar (S ou N)")
                continue
    except ValueError as ve:
        return str(ve)       
 
##-----------------------------------------------------
##----------------------------------------------------- 
  
def createApostQ(nu, max, mod): 
    lista = list()
    jogos = list()
    print('-' * 70)
    print(' '*20, f'JOGAR {mod}',' '*20)
    print('-' * 70)

    cont = 0
    while True:
        num = rd.randint(1, max) 
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= nu:
            break
    lista = sorted(lista)
    jogos.append(lista[:])
    ID = NewID.GetID()
    
    #for i, l in enumerate(jogos):
    #   print(f'Jogo {i} - {ID}: {l}')
    SixApostMega(nu, max, lista)
    
##-----------------------------------------------------
##-----------------------------------------------------

def SixApostMega(nu, maximo, mod): 
    lista = list()
    jogos = list()
    
    quant = max(mod)
    quant += 1
    tot = 1

    while tot <= quant:
        cont = 0
        while True:
            num = rd.randint(1, maximo) 
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= nu:
                break
        lista = sorted(lista)
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    ID = NewID.GetID()
    print('-='*5,f' SORTEANDO {max(mod)} JOGOS ', '=-'*5)   
    for i, l in enumerate(jogos):       
        if i in mod:
           print(f'Jogo {i} - {l}')      
        #sleep(2)  
    print('-='*5, '< BOA SORTE!>', '=-'*5)