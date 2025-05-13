import json
import urllib.request
import os
import src.services.SystemVersions as SystemVersions
from rich.progress import track
from time import sleep
import src.services.NewID as NewID
import src.services.ClearScren as ClearScren
import src.controller.ConsultOne as ConsultOne
import src.services.NewResult as Get
import src.services.SaveFile as dbb
import src.services.SelectFile as dba
import src.report.AnalityArkivo as AA

def Apost(Concurso, Loterias):
  text = "" 
  try:
      ID = NewID.GetID()           
      
      SystemVersions.print_version()
      if Concurso == 'latest': 
        for t in track(range(5), f'Processando...'):
          sleep(0.5)             
        print("Use a Função consultar ultimo registro")
      else:
        for t in track(range(5), f'Processando... {Get.get_numero(Loterias,Concurso)}'):          
          sleep(0.5)        
        loterias_jogos = Get.ResultApost(Loterias,Concurso)
        #print(Get.get_numero(Loterias,Concurso), '==>>', (Get.get_numero(Loterias,Concurso)/60), '-Min')
        dbb.SaveFile.SalvarMoreResult(ID, Loterias, loterias_jogos)       

  except ValueError as ve:
        print(f'O Concurso {Concurso} não existe', str(ve))
#****************************************************************************************************************************        
#**************************************************************************************************************************** 
def GetAll():
  ClearScren.cls()
  ret = ConsultOne.MsgJogos() 
  if ret != "error" :
    x = int(input(f'Digite Concurso DE: '))
    qty = int(input(f'Digite Concurso Até: '))  
    if x == 0:
      x = 'latest'     
      Apost(x, ret)
    else:  
      while x <= qty:            
        Apost(x, ret)
        x += 1
      print('Finalizado Com Sucesso')

#****************************************************************************************************************************        
#**************************************************************************************************************************** 
def UpDateAll():
  ClearScren.cls()
  nine = ['MegaSena', 'LotoFacil', 'Quina', 'LotoMania', 'TimeMania', 'DuplaSena', 'Federal', 'DiadeSorte', 'SuperSet']
  ret = ConsultOne.MsgJogos() 

  if ret in nine:
    x = LeftArquivo(ret)
    x += 1
    qty = LeftConcurso(ret) 
    if x <= qty:   
      while x <= qty:            
        Apost(x, ret)
        x += 1
    print('Finalizado Com Sucesso')  
  elif ret == "ThreeGames" :
      three = ['MegaSena', 'LotoFacil', 'Quina']
      for game in three:         
          MsgBuild(game)
          x = LeftArquivo(game)
          x += 1
          qty = LeftConcurso(game) 
          if x <= qty:   
            while x <= qty:            
              Apost(x, game)
              x += 1
      print('Finalizado Com Sucesso')
#****************************************************************************************************************************        
#**************************************************************************************************************************** 
def MsgBuild(game):
  if game == 'MegaSena':
    i=1
  elif game == 'LotoFacil':
    i=2
  elif game == 'Quina':
    i=3
  else:
    i=0
  print(f'Build start for application between @-{i}-# and @-{i}-# start now !!!')
#****************************************************************************************************************************        
#****************************************************************************************************************************
def LeftArquivo(string_input):
  try:       
      content = dba.SelectFile.ReadFileResult(string_input)
      last_line = content[-1]      
      Id_Find = AA.Validationfind(last_line)     
      return Id_Find
  except FileNotFoundError:
      print(f'O arquivo {string_input} não existe!')        
#****************************************************************************************************************************        
#**************************************************************************************************************************** 
def LeftConcurso(Loterias):
  try: 
    cod = Get.UltmResult(Loterias)
    return cod.numero()
  except FileNotFoundError:
      print(f'O arquivo {Loterias} não existe!')
#GetAll()