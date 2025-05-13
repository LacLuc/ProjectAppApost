import src.services.ClearScren as ClearScren
import src.report.AnalityThree as AnalityThree
import AnalityALL
import MoreResult
import src.report.AllConcurso as AllConcurso
import src.report.AnalityArkivo as AnalityArkivo
from colorama import Back, Fore, Style, init

def AnalisesApp():
    ClearScren.cls()
    while True:
        process = input(Fore.YELLOW +
        "--------------------------------\n"
        "|###  Menu Aportes - Budget  ##|\n"
        "| 1 - ApostThree               |\n"
        "| 2 - NormaProbality           |\n"
        "| 3 - AllProbality             |\n"
        "| 4 - Qtde_Gerada              |\n"
        "| 5 -                          |\n"
        "| 6 -                          |\n"
        "| 7 - Analisar_Concurso        |\n"
        "| 8 - Analisar_AllConcurso     |\n"
        "| 9 - UpDateJogos              |\n"
        "| 0 - Sair :                   |\n"
        "--------------------------------\n"
        "==>> ")
        if process == '':
            process = 0                   

        if process == '1' or process == 'ApostThree':
            AnalityThree.ApostThree()
        elif process == '2' or process == 'NormaProbality':         
            AnalityThree.NormaProbality()
        elif process == '3' or process == 'AllProbality':
            AnalityALL.gera_jogos()
        elif process == '4' or process == 'Qtde_Gerada':
            AnalityALL.QtdeRegistros()
        elif process == '7' or process == 'Analisar_Concurso':    
            AnalityArkivo.AnalityConcurso()   
        elif process == '8' or process == 'Analisar_AllConcurso':    
            validator = AllConcurso.IDValidator()
            validator.AnalityConcurso()
        elif process == '9' or process == 'UpDateJogos':
            MoreResult.UpDateAll()
        elif process == 0 or process == '0':
            ClearScren.cls()
            break    
        else:
            print("Você deve informar um processo validao!")   