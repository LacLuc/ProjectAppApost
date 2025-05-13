#----------------------------------------------
#----------------------------------------------

from random import sample
from time import sleep
import datetime 
import src.services.NewID as NewID
import re
import src.services.SaveFile as dbb

#import LotoFacil

def horarioBR():
    now = datetime.datetime.now()    
    print(" "*70)
    print(f'Data: {now.day}/{now.month}/{now.year} - {now.hour}:{now.minute}')
##################################################################################################

def AddNumerosJogos():
    AddObj = []
    AddTuentyFive = []
    #VldObj = range(1, 26)
    AddTuentyFive = sample(range(1, 26), 25)  
    AddTuentyFive.sort()
    
    Ob = input('Deseja Informa os Numeros? (S ou N) ')
    if Ob == 'S' or Ob == 's':
        FuncStatus = 2        
        while FuncStatus == 2:
            Inicio_Jogos = int(input('Quantos numero pretende preencher? (1 até 20): '))    
            if Inicio_Jogos in range(1, 21):            
                if Inicio_Jogos < 15:  
                    fon = abs(Inicio_Jogos - 15)                  
                    AddObj = PreencherNum(Inicio_Jogos, AddTuentyFive, AddObj)
                    
                    for item in AddObj:
                        if item in AddTuentyFive:
                            AddTuentyFive.remove(item) 
                
                    ObjRef = sample(AddTuentyFive, fon)

                    for i in ObjRef:
                        AddObj.append(i)

                elif Inicio_Jogos >= 15 and Inicio_Jogos <= 20:                                       
                    AddObj = PreencherNum(Inicio_Jogos, AddTuentyFive, AddObj)                  
                else:
                    print(f'Este numero {Inicio_Jogos} não é valido')

                FuncStatus = 1
            else:
                print(f'Este numero {Inicio_Jogos} não é valido')
                FuncStatus = 2

    else:  #Se for informado Sim será feito esta etapa.       
        AddObj = sample(range(1, 26), 15)    
    return AddObj    
##################################################################################################

def PreencherNum(Inicio_Jogos, AddTuentyFive, AddObj):
    s = 1
    while s <= Inicio_Jogos:
        ObjR = int(input(f'Digite o {s}º Numero: '))
        if ObjR in AddTuentyFive:
            AddObj.append(ObjR)                            
            s += 1
        else:
            print(f'Este numero {ObjR} não é valido ou já foi usado!')
    return AddObj
##################################################################################################

def Analisy():
  
  horarioBR()
  qty = int(input('Quatos jogos: '))
  print(" "*70)
  
  Y = 1
  obj = []
  obj = AddNumerosJogos()
  obj.sort()
  
  ID = NewID.GetID()

  print('<='*5, f'Jogo: Principal', '=>'*5)  

  print(f'Jogo: {obj}')
  t = sum(obj)
  maxi = max(obj) 
  mini = min(obj)
  
  Ref1 = f'Jogo: {obj}'
  Ref2 = f'Maxímo: {maxi}'
  Ref3 = f'Minimo: {mini}'
  Ref4 = f'Soma_Total: {t}'
  dbb.SaveFile.SalvarFiles(ID, Ref1, Ref2, Ref3, Ref4)

  print(f'Maxímo: {maxi}')
  print(f'Minimo: {mini}')
  print(f'Soma_Total: {t}')    
  #def Quase_Functiom
  ##################################################################################################
  
  spel = input('Espelho Automático? (S ou N) ')
  espelho = []
  if spel == 'S' or spel == 's':
      espelho = sample(obj, 5)
      espelho.sort()
  else:
      fon = 5
      s = 1
      while s <= fon:
        EA = int(input(f'Digite o {s}º Numero: '))
        
        if EA in obj:
           espelho.append(EA)
           s += 1
        else:
           print(f'Este numero {EA} não é valido')
          
  print(" "*70)
  onEspelho = 'OneProcess'  
  while Y <= qty:  
    base = list(range(1, 26))
        
    print('<='*5, f'Jogo: {Y}', '=>'*5)

    if onEspelho == 'OneProcess':
        for item in obj:
            if item in base:
                base.remove(item)

        for i in espelho:
            base.append(i)
            
        base.sort()  
        
        print(f'5_Jogos_Espelho: {espelho}')
        print(f'Espelho: {base}')

        t = sum(base)
        maxi = max(base) 
        mini = min(base)
        
        Ref1 = f'Espelho: {base}'
        Ref2 = f'Maxímo: {maxi}'
        Ref3 = f'Minimo: {mini}'
        Ref4 = f'Soma_Total: {t}'
        dbb.SaveFile.SalvarFiles(ID, Ref1, Ref2, Ref3, Ref4)

        print(f'Maxímo: {maxi}')
        print(f'Minimo: {mini}')
        print(f'Soma_Total: {t}')
        print(" "*70)
        onEspelho = 'TwoProcess'
    else:              
        for item in espelho:
            if item in base:
                base.remove(item)

        TwoBase = sample(base, 10)
            
        for i in espelho:
            TwoBase.append(i)
            
        TwoBase.sort()  
        
        
        print(f'5_Jogos_Espelho: {espelho}')
        print(f'Espelho: {TwoBase}')

        t = sum(TwoBase)
        maxi = max(TwoBase) 
        mini = min(TwoBase)
        
        Ref1 = f'Espelho: {TwoBase}'
        Ref2 = f'Maxímo: {maxi}'
        Ref3 = f'Minimo: {mini}'
        Ref4 = f'Soma_Total: {t}'
        dbb.SaveFile.SalvarFiles(ID, Ref1, Ref2, Ref3, Ref4)

        print(f'Maxímo: {maxi}')
        print(f'Minimo: {mini}')
        print(f'Soma_Total: {t}')
        print(" "*70)    
    Y += 1
