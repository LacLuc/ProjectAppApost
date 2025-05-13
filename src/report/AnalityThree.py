import random, os
from time import sleep
from rich.progress import track

def ApostThree():
    lists = []
    lista = []
    listas = []
    z = 1
    qty = 5
    vh = input('Vertical ou Horisontal (v e h): ')
    while z <= qty:
        if z == 1:
            fiveIN = VH(z, vh)
        elif z ==2:
            fiveIN = VH(z, vh)
        elif z ==3:
            fiveIN = VH(z, vh)
        elif z ==4:
            fiveIN = VH(z, vh)
        elif z ==5:
            fiveIN = VH(z, vh)
        else:
            print('Max Nro')    

        x = obter_valor_aleatorio(fiveIN)
        #print(f"Valor aleatório: {x}")
        
        if x not in lista:
            lista.append(x)
            lista.sort()
        if len(lista) >= 3:
            t = 0
            while t == 0:
                for r in lista:
                    if r not in listas:
                        listas.append(r)
                        lista.sort()
                    if len(listas) >= 3:
                        lists.append(listas)
                        #lists = '\n'.join(lists)
                        t+=1
                        z+=1
                        lista = []
                        listas = []
            #os.system('cls')
    print(lists)

def obter_valor_aleatorio(lista):
    return random.choice(lista)

def VH(n, vh):
    if n == 1:
        if vh == 'v':
            list1 = [1, 6, 11, 16, 21]
        else:
            list1 = [1, 2, 3, 4, 5] 
        return list1 
    elif n == 2:
        if vh == 'v':        
            list2 = [2, 7, 12, 17, 22]
        else:    
            list2 = [6, 7, 8, 9, 10]
        return list2
    elif n == 3:
        if vh == 'v':
            list3 = [3, 8, 13, 18, 23]
        else:
            list3 = [11, 12, 13, 14, 15]
        return list3
    elif n == 4:
        if vh == 'v':
            list4 = [4, 9, 14, 19, 24]
        else:    
            list4 = [16, 17, 18, 19, 20]
        return list4
    elif n == 5:
        if vh == 'v':
            list5 = [5, 10, 15, 20, 25]
        else:   
            list5 = [21, 22, 23, 24, 25] 
        return list5

############################################################################################

def NormaProbality():
    t = 1
    qty = int(input('Digite qyde: '))
    while t <= qty:
        lista =[]
        for i in range(25):
            x = random.random()
            vlr = round(x, 2)
            lista.append(vlr)
        print(lista)
        t +=1    