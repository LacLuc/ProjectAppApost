import src.services.SaveFile as dbb
import src.services.NewID as NewID
import random as rd
from time import sleep
#--------------------------------------------------
#--------------------------------------------------
def newApost(nu, max, mod): 

    lista = list()
    jogos = list()

    print('-' * 70)
    print(' '*20, f'JOGAR {mod}',' '*20)
    print('-' * 70)
    quant = int(input('Digite Qtde de Jogos: '))
    tot = 1

    while tot <= quant:
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
        lista.clear()
        tot += 1
    ID = NewID.GetID()
    print('-='*5,f' SORTEANDO {quant} JOGOS ', '=-'*5)   
    for i, l in enumerate(jogos):        
        print(f'Jogo {i+1} - {ID}: {l}')      
        dbb.SaveFile.SalvarDadosFilas(ID, l)
        sleep(2)  
    print('-='*5, '< BOA SORTE!>', '=-'*5)

#--------------------------------------------------
#--------------------------------------------------
def ApostSimplo(nu, max, mod): 
    lista = list()
    jogos = list()
    trevo = list()
    print('-' * 70)
    print(' '*20, f'JOGAR {mod}',' '*20)
    if mod == 'Milionária' or mod == 'milionária':
        print('A MILIONÁRIA é uma loteria diferente,')
        print('onde você escolhe 6 números no campo composto por 50')
        print('e escolhe também 2 trevos numerados no espaço contendo 6.')
        print('https://loterias.caixa.gov.br/Paginas/mais-milionaria.aspx')

    print('-' * 70)
    quant = int(input('Digite Qtde de Jogos: '))
    tot = 1

    while tot <= quant:
        cont = 0
        while True:
            num = rd.randint(1, max) 
            if num not in lista:
                lista.append(num)
                cont += 1
            if cont >= nu:
                break
        lista = sorted(lista)

        cont = 0
        while True:
            num = rd.randint(1, 6) 
            if num not in trevo:
                trevo.append(num)
                cont += 1
            if cont >= 2:
                break
        trevo = sorted(trevo)
        jogos.append('Start')
        jogos.append(lista[:])
        jogos.append('Trevo')
        jogos.append(trevo[:])
        jogos.append('End')
        trevo.clear()
        lista.clear()
        tot += 1      

    obj = 0
    print('-='*5,f' SORTEANDO {quant} JOGOS ', '=-'*5)   
    for i, l in enumerate(jogos):
        if l == 'Trevo':
          print('Trevo')
        elif l == 'Start': 
          obj += 1
        elif l == 'End': 
          print('-' * 70)    
        else:
          print(f'Jogo {obj}: {l}')      
          sleep(2)  
    print('-='*5, '< BOA SORTE!>', '=-'*5)

#--------------------------------------------------
#--------------------------------------------------
def NewInput(): 
    Mega = 'Mega'
    Loto = 'Loto'
    Quina = 'Quina'
    Milionaria = 'Milionaria'
    print(f'1 = {Mega}')
    print(f'2 = {Loto}')
    print(f'3 = {Quina}')
    print(f'4 = {Milionaria}')
    Qjogo = input('digite o tipo de jogo: ')
    if Qjogo == 'Mega' or Qjogo == 'mega' or Qjogo == '1':
        newApost(6,60,'MEGA SENA') #aposta Mega
    elif Qjogo == 'Loto' or Qjogo == 'loto' or Qjogo == '2':
        newApost(15,25,'LOTO FÁCIL') #aposta Loto
    elif Qjogo == 'Quina' or Qjogo == 'quina' or Qjogo == '3':
        newApost(5,80,'QUINA')  #aposta Quina
    elif Qjogo == 'Milionaria' or Qjogo == 'milionaria' or Qjogo == '4':
        ApostSimplo(6,51,'Milionária')  #aposta Quina  
    else:
        print("Modalidade de aposta não informada ou não existe")