import os
import src.services.ClearScren as ClearScren
import src.controller.ConsultOne as ConsultOne
import src.services.SelectFile as dba
import json
#-------------------------------------------------------------
def NumberCount(string_input):
    try:       
        content = dba.SelectFile.ReadFileResult(string_input)
        last_line = content[-1]
        print(last_line)
    except FileNotFoundError:
        print(f'O arquivo {string_input} não existe!')


def definitionJogo():
    ClearScren.cls()
    print('-='*5,' Cunsultar_Ultimo_Registro ', '=-'*5)
    Loterias = ConsultOne.MsgJogos()
    NumberCount(Loterias)

