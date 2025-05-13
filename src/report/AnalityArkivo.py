import re
import src.services.ClearScren as ClearScren
import src.controller.ConsultOne as ConsultOne
import src.model.MsgAnalityArkivo as Msg
import src.services.ConverterBase as Conv
import src.services.SelectFile as dba
import src.services.SaveFile as dbb

def NumberCount(string_input):    
    lista = []
    listConcurso = []
    AppBinario = input('Aplicação Binaria (n ou s) : ')
    if AppBinario == 's' or AppBinario == 'S':
        sv = input('Deseja Salvar o Binario (n ou s) : ')    
    else:
        sv = 'n'    
    ClearScren.cls()
    print('-='*5,' Analisar_Concurso ', '=-'*5)
    n = ValQualJogo(string_input)
   
    content = dba.SelectFile.ReadFileResult(string_input)
    listConcurso = QProcessRun()
    listConcurso.sort()    
    for con in content:  
        Id_Find = Validationfind(con)
        if Id_Find > max(listConcurso):
            break
        for LC in listConcurso:
            if LC == Id_Find:                    
                #print(con)                        
                numVws = 0
                NewList = formatList(con)
                if AppBinario == 's' or AppBinario == 'S':
                    #Neste ponto o Sistema começa uma logica para criar o Binario.
                    Binario = CreateBinario(NewList, numVws, lista, n)
            
                    #Salvar o Arkivo Binario
                    nome = createNome(Binario, LC)
                
                    if sv == 's' or sv == 'S':
                        SalverArkivo(n, nome, Binario)
                else:
                    nome = str(LC).zfill(6),NewList
                print(nome)
                #print(f'{(str(LC).zfill(6),lista)}')
                lista.clear() 
                #print(NewList) 



def createNome(Binario, LC):
    b = str(LC).zfill(6),Binario
    b = str(b) 
    b = b.replace("'","").replace("(","").replace(")","").replace(", ",", '")  
    return b


def CreateBinario(NewList, numVws, lista, n):
    for vowels in range(1,n):                    
        Qty = ContadorComparador(NewList, vowels, numVws)
        lista.append(Qty)    
    x = lista  
    x = str(x)                   
    x = x.replace("[","").replace("]","").replace(",","").replace("(","").replace(")","").replace("'","")
    Binario = x.replace(" ","")            
    return Binario



def SalverArkivo(n,nome,Binario):
    #db.AppSalvar(f"{nome}")    
    if n == 81:
        dbb.SaveFile.SalvarBinario(nome, 'Quina')
    elif n == 26:
        nome = nome, Conv.bin_to_quaternary(Binario), Conv.bin_to_octal(Binario), Conv.bin_to_dec(Binario), Conv.bin_to_hex(Binario)   
        nome = str(nome) 
        nome = nome.replace("'","").replace("(","").replace(")","").replace('"','').replace(", ",", '")  
        dbb.SaveFile.SalvarBinario(nome, 'LotoFacil')   
    elif n == 61:
        dbb.SaveFile.SalvarBinario(nome, 'MegaSena')    


def ValQualJogo(string_input):
    if string_input == 'Quina':
        return 81
    elif string_input == 'LotoFacil':
        return 26   
    elif string_input == 'MegaSena':
        return 61   
    else:
        return 0                
                                       
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

def Validationfind(con):
    match = re.search(r"\((\d+),", con)
    if match:
        numeros = match.group(1)
        return int(numeros)

def QProcessRun():    
    lst = []
    print(Msg.MsgRange())
    print(Msg.MsgUmAUm())
    ran = int(input(Msg.MsgProcesso()))
    if ran == 1:
        x = int(input(Msg.MsgConcursoDE()))
        qty = int(input(Msg.MsgConcursoAte())) 
        while x <= qty:    
            lst.append(x)
            x += 1
    else:   
        Qn = 1
        n = int(input(Msg.MsgQtyProcesso())) 
        while Qn <= n:
            Xn = int(input(Msg.MsgNumeroConcurso(Qn)))
            lst.append(Xn)             
            Qn += 1     
    return lst           

#NumberCount('Result_MegaSena')
#NumberCount('Result_LotoFacil')
#NumberCount('Result_Quina')

def AnalityConcurso():
    ClearScren.cls()
    print('-='*5,' Analises_Concurso ', '=-'*5)
    Loterias = ConsultOne.MsgJogos()
    NumberCount(Loterias)