import json
import urllib.request
from time import sleep
import src.services.NewID as NewID
import src.services.NewResult as Get
import src.services.ClearScren as ClearScren
from colorama import Back, Fore, Style, init

def Apost(Concurso, Loterias):
  text = ""
  try:
      if Concurso == 'latest':
        cod = Get.UltmResult(Loterias)
        Qual = input('Todos os dados (s ou n): ')
        if Qual == 's':
          print(json.dumps(cod.todosDados(), ensure_ascii=False, indent=2))
        else:
          print(cod.numero(), cod.dataApuracao(), cod.listaDezenas())
      else: 
          #ID = NewID.GetID()            
          Qual = input('Todos os dados (s ou n): ')
          if Qual == 's':
            Delta = Get.ResultDelta(Loterias,Concurso)
            print(json.dumps(Delta.todosDados(), ensure_ascii=False, indent=2))
          else:          
            loterias_jogos = Get.ResultApost(Loterias,Concurso)      
            print(loterias_jogos)     

  except ValueError:
        print(f'O Concurso {Concurso} não existe')
#--------------------------------------------------
#--------------------------------------------------

def MsgJogos():
  ClearScren.cls()
  while True:
      Result = input(Fore.GREEN +
        "--------------------------------\n"
        "|###  Menu Aportes - Budget  ##|\n"
        "| 1 - MegaSena:                |\n"
        "| 2 - LotoFacil:               |\n"
        "| 3 - Quina:                   |\n"
        "| 4 - LotoMania:               |\n"
        "| 5 - TimeMania:               |\n"
        "| 6 - DuplaSena:               |\n"
        "| 7 - Federal:                 |\n"
        "| 8 - DiadeSorte:              |\n"
        "| 9 - SuperSet:                |\n"
        "| 10- ThreeGames               |\n"
        "--------------------------------\n"
        "==>> ")
  
  
      Mega = 'MegaSena'
      Loto = 'LotoFacil'
      Quina = 'Quina'
      Lotomania = 'LotoMania'
      Timemania = 'TimeMania'
      DuplaSena = 'DuplaSena'
      LoteriaFederal = 'Federal'
      DiaDeSorte = 'DiadeSorte'
      SuperSete = 'SuperSet'
      ThreeGames = 'ThreeGames'
      
      if Result == '1' or Result == Mega:
        return Mega
      elif Result == '2' or Result == Loto:
        return Loto
      elif Result == '3' or Result == Quina:
        return Quina
      elif Result == '4' or Result == Lotomania:
        return Lotomania
      elif Result == '5' or Result == Timemania:
        return Timemania
      elif Result == '6' or Result == DuplaSena:
        return DuplaSena    
      elif Result == '7' or Result == LoteriaFederal:
        return LoteriaFederal
      elif Result == '8' or Result == DiaDeSorte:
        return DiaDeSorte 
      elif Result == '9' or Result == SuperSete:
        return SuperSete         
      elif Result == '10' or Result == ThreeGames:
        return ThreeGames
      else:
        print(f'Esta Loteria {Result} não existe') 
        return "error" 
#--------------------------------------------------
#--------------------------------------------------
    
def GetJogos():
  Loterias = MsgJogos() 
  if Loterias != "error" :
      Concurso = int(input(f'Digite Concurso: '))
      if Concurso == 0:
        Concurso = 'latest'
      Apost(Concurso, Loterias)  
      print('Finalizado Com Sucesso')
#GetJogos()   