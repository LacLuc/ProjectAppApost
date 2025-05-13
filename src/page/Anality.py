import os
import src.services.ClearScren as ClearScren
import src.controller.ConsultOne as ConsultOne
import src.services.SelectFile as dba
#-------------------------------------------------------------
def AnalityNumber(string_input):
    try:
        content = dba.SelectFile.ReadFileResult(string_input)
        ForAnality(content)
        last_line = content[-1]
        print(last_line)
    except FileNotFoundError:
        print(f'O arquivo {string_input} não existe!')


def ForAnality(content):
    num = [1]
    lista_nro = [n for n in content if n in num]
    print(lista_nro)


def AnalityJogo():
    ClearScren.cls()
    print('-='*5,' Analises_Registros ', '=-'*5)
    Loterias = ConsultOne.MsgJogos()
    AnalityNumber(Loterias)

#AnalityJogo()