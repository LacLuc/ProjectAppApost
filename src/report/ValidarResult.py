import src.controller.ConsultOne as ConsultOne
import re
import src.services.NewResult as Get
import src.services.ClearScren as ClearScren
import src.services.SelectFile as dba

def NumberCount(string_input):  
    content = dba.SelectFile.ReadFile(string_input)
    num_records = len(content)
    print(f"Qty de registros no arquivo de 0 até {num_records-1}")
    n = int(input('Digite a posição para conferir: '))
    last_line = content[n]
    last_line = converter_para_lista(last_line)
    return last_line

def converter_para_lista(sequencia):
    # Dividir a string em uma lista de strings de números
    numeros_str = sequencia.split()
    # Converter cada string de número em um inteiro e retornar a lista
    return [int(numero) for numero in numeros_str]


def resultOfApost():
  Loterias = ConsultOne.MsgJogos()
  Concurso = int(input(f'Digite Concurso: '))
  if Concurso == 0:
    cod = Get.UltmResult(Loterias)
  else:
    cod = Get.Result_func(Loterias,Concurso)
  print(f'Resultado: {cod.numero()}')
  lista = cod.listaDezenas()
  #lista_formatada = [value.lstrip('0') for value in lista]
  #resultado = ' '.join(lista_formatada)
  lista = [int(numero) for numero in lista]
  print(f'{lista} Nr: {len(lista)}')
  return lista
  

def conferir_aposta_lotofacil(aposta, resultado_sorteio):
    # Calcula a interseção dos conjuntos para encontrar os números corretos
    acertos = []
    for i in resultado_sorteio:
      for j in aposta:
        if j == i:
          acertos.append(i)
    return acertos


def vldResult(x):  
  if x == 's0':
    ClearScren.cls()
  print(' '*18, f'INICIO DA CONFERENCIA',' '*18)
  aposta = NumberCount('ArkivotTopFive')
  resultado_sorteio = resultOfApost()
  print(f'{aposta} Nr: {len(aposta)}')
  quantidade_acertos = conferir_aposta_lotofacil(aposta, resultado_sorteio)
  print(quantidade_acertos)
  print(f'Você acertou {len(quantidade_acertos)} números!')

