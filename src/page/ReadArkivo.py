
import re
import src.services.SelectFile as dba

def NumberCount(string_input):
    lista = []
    content = dba.SelectFile.ReadFile(string_input)
    for con in content:    
        #vowels = "05"
        numVws = 0
        for vowels in range(1,26):
            NewList = formatList(con)
            Qty = ContadorComparador(NewList, vowels, numVws)
           #TODO: Fazer a chamada da lista par add e devolver
            #lista.append(f'{vowels},{Qty}')
            lista.append(Qty)           
        print(lista)
        print(NewList)
            
    ListaBaseX = formatList(lista)
    print(ListaBaseX)

def ContadorComparador(NewList, vowels, numVws):
    for x in NewList:                
        if( int(vowels) == int(x)):
            numVws += 1
            break
    return numVws       

def formatList(con): #Limpa os dados e retorna uma lista.
    numbers = re.findall(r'\[(.*?)\]', con)
    lista = '\n'.join(numbers)
    list = lista.split(',')
    nova_string  = [item.strip().strip("'") for item in list]
    return nova_string

'''
def Count_NumR(string_input):
    Cont = 0
    content = dba.SelectFile.ReadFile(string_input)
    for con in content:           
        numbers = re.findall(r'\[(.*?)\]', con)
        removed_chars = ['.', ',', '!', '[', ']']
        chars = set(removed_chars)        
        s = ''.join(filter(lambda x: x not in chars, numbers))         
        res = re.sub('[.,!]', '', s)            
        print(res)
'''       

#Count_NumR(input('Digite o Arquivo: '))
#NumberCount(input('Digite o Arquivo: '))
NumberCount('Result_lotofacil')
#Result_lotofacil