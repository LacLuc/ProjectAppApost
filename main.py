#-*-coding:utf8;-*-
#qpy:console

# import ApostSemple
from rich.progress import track
from time import sleep
# import MoreResult
# import ConsultOne
# import TopFive
# import MegaSix
# import QuinaFive
import sys
# import ConsultConcurso
import src.services.ClearScren as ClearScren
# import ValidarResult
# import UpBiblioteca
# import Core
from colorama import Back, Fore, Style, init

#--------------------------------------------------
#--------------------------------------------------      
def StylerApost(x):
    ClearScren.cls()
    while True:
        process = input(Fore.CYAN +
        "--------------------------------\n"
        "|###  Menu Aportes - Budget  ##|\n"
        "| 1  - Aposta:                 |\n"
        "| 2  - Resultado:              |\n"
        "| 3  - Consulta:               |\n"
        "| 4  - ApostaEspelho:          |\n"
        "| 5  - ApostaQuinaFive:        |\n"
        "| 6  - ApostaMegaSix:          |\n"
        "| 7  - Cunsultar_resultados    |\n"
        "| 8  - Ultimo_Registro         |\n"
        "| 9  - Core_V1                 |\n"      
        "| 999 -                        |\n"
        "| 0 - Sair :                   |\n"
        "--------------------------------\n"
        "==>> ")
        if process == '':
            process = 0                   

        if process == '1' or process == 'Aposta':
            '''TODO:'''
            #ApostSemple.NewInput()
        elif process == '2' or process == 'Resultados': 
            '''TODO:'''
            #MoreResult.GetAll()
        elif process == '3' or process == 'Consulta': 
            '''TODO:'''
            #ConsultOne.GetJogos()
        elif process == '4' or process == 'ApostaEspelho': 
            '''TODO:'''
            #TopFive.Analisy()
        elif process == '5' or process == 'ApostaQuinaFive':
            '''TODO:'''
            #QuinaFive.newApostQuina(5,80,'QUINA')  #aposta Quina
        elif process == '6' or process == 'ApostaMegaSix':
            '''TODO:'''
            #MegaSix.newApostMega(6, 60, 'Mega')
        elif process == '7' or process == 'Cunsultar_resultados':     
            '''TODO:'''
            #ValidarResult.vldResult(x)
        elif process == '6' or process == 'Ultimo_Registro':
            '''TODO:'''
            #ConsultConcurso.definitionJogo()
        elif process == '9' or process == 'Core_V1':    
            '''TODO:'''
            #Core.AnalisesApp()        
        elif process == '99' or process == 'UP_Biblioteca':
            # Exemplo de uso da função -- 'loteria-caixa'
            Bibli = input('Digite o Biblioteca para ser Atualizada: ')
            '''TODO:'''
            #UpBiblioteca.verificar_atualizacao(Bibli)   
        elif process == 0 or process == '0':
            ClearScren.cls()
            break    
        else:
            print("Você deve informar um processo validao!")         

#--------------------------------------------------
#--------------------------------------------------  
def Processando():
    Msg = 'Processando...'
    return Msg        

def MsgFinaladoApp():
    Msg = '-='*5, '< Sistema finalizado! >', '=-'*5
    return Msg

#--------------------------------------------------
#--------------------------------------------------  
def main():
    ClearScren.cls()
    x = 's1'
    try:
        while True:
            Status = input('Deseja Continuar... (S ou N): ')
            if Status.lower() in ('s', 's0'):
                if Status == 's0':
                    ClearScren.cls()
                    x = Status
                else:
                    x = 's1'
                StylerApost(x)
            elif Status.lower() == 'n':
                ClearScren.cls()
                for t in track(range(5), Processando()):
                    sleep(1)
                print(MsgFinaladoApp())
                break
            else:
                ClearScren.cls()
                print("Você deve informar (S ou N)")
    except ValueError as ve:
        return str(ve)

if __name__ == '__main__':
   sys.exit(main())

