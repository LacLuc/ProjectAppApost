import re
import src.services.ClearScren as ClearScren
import src.controller.ConsultOne as ConsultOne
import src.services.SelectFile as dba
import src.services.SaveFile as dbb
import src.report.AnalityArkivo as Aty

class IDCycleApost:
    def __init__(self):
        self.probaby = set() 
                

    def AnalityConcurso(self):
        ClearScren.cls()
        print('-='*5,' Analises_Ciclo_Concurso ', '=-'*5)
        #Loterias = ConsultOne.MsgJogos()
        Loterias = "LotoFacil"
        if Loterias == "LotoFacil":
            cycle = IDCycleApost()
            cycle.CycleCount(Loterias)
        else:
            print("Apenas a Loto esta cadastrada!")    
            
            
    def CycleCount(self, string_input):
        try:
            cycle = IDCycleApost()         
            cycle.load_data(string_input)
            cycle.validate_and_register()            
        except ValueError:
            print(f'Existe Um Erro')
    
    
    def load_data(self, string_input):               
        self.content = dba.SelectFile.ReadFileResult(string_input)
        self.Cycle = dba.SelectFile.selectCycle()
    
    def validate_and_register(self):
        InCycle = []
        cycle = IDCycleApost() 
        contesto = self.content
        for con in contesto:            
            DadosCycle = dba.SelectFile.selectCycle()     
            results = cycle.extrair_dados(con)       # Apenas os numeros do Resultado
            Id_Result = Aty.Validationfind(con)  
            for cys in DadosCycle:
                idConcurso = int(cycle.OUC(cys, 'Concurso'))
                if idConcurso == '':                   
                    InCycle = cycle.verificQCycleTwo(results)
                    self.ControFull(InCycle, cycle, DadosCycle, results, Id_Result)
                elif Id_Result > idConcurso:
                    InCycle = cycle.verificQCycleOne(DadosCycle,results)                    
                    self.ControFull(InCycle, cycle, DadosCycle, results, Id_Result)
                else:
                    continue


    def ControFull(self, InCycle, cycle, DadosCycle, results, Id_Result):
        fullCycle = cycle.CycleInput(results, InCycle)
        cycle.SaveReport(Id_Result, fullCycle, DadosCycle)
        if len(fullCycle) == 25:
            InCycle = []
            
            
    def verificQCycleOne(self, DadosCycle, results):
        id = 1
        bdados = []
        if DadosCycle != []:            
            for cy in DadosCycle:
                id_cy = int(cycle.OUC(cy, 'Ciclo'))
                if id_cy >= id:
                    ffdados = cycle.extrair_dados(cy)
                    for i in ffdados:
                        bdados.append(i)
                    for i in results:    
                        if i not in bdados: 
                            bdados.append(i)    
                        
        elif DadosCycle == []:        
            bdados = results    
        bdados.sort()
        return bdados
            
            
    def verificQCycleTwo(self, results):        
        bdados = []
        for i in results:
            bdados.append(i) 
        return bdados
    
    
    def SaveReport(self, Id_Result, fullCycle, DadosCycle):    
        cycle = IDCycleApost()      
        if len(fullCycle) == 25:
            Id_Cycle += 1    
        else:        
            Id_Cycle = cycle.IdCycle(DadosCycle)
            
        meu_dicionario = {
            "Ciclo": str(Id_Cycle).zfill(6),
            "Concurso": str(Id_Result).zfill(6),
            "AcertoCiclo": str(len(fullCycle)),
            "Jogos": str(fullCycle)
        }            
            
        refCycle = cycle.VldCycle(Id_Result, DadosCycle)
        if refCycle == 1:
            print(meu_dicionario)
            dbb.SaveFile.SeveCycle(meu_dicionario)            
            
            
    def VldCycle(self, Id_Result, DadosCycle):
        cycle = IDCycleApost()            
        for cy in DadosCycle:
            id_cy = cycle.OUC(cy, 'Concurso:')
            if Id_Result == id_cy:
                return 0
        return 1      
    
    
    def IdCycle(self, DadosCycle):
        cycle = IDCycleApost()   
        Id_Cycle = 1                   
        for cy in DadosCycle:
            id_cy = int(cycle.OUC(cy, 'Ciclo'))
            if  id_cy >= Id_Cycle:
                return id_cy
        return Id_Cycle      
    
            
    def OUC(self, dados, Regist):
        if dados != '\n':    
            if "[" not in dados and "]" not in dados and "\n" not in dados:
                dados_limpos = dados                
            else:
                # Remove os caracteres indesejados da string
                dados_limpos = dados.strip("[] \n")
                
            if dados != '':   
                # Converte a string em um dicionário
                dicionario = eval(dados_limpos)
                
                # Obtém o valor do 'Ult_Concurso'
                ultimo_concurso = dicionario.get(Regist)
        else:
            ultimo_concurso = 0
        return ultimo_concurso        
            
            
    def extrair_dados(self, texto):
        # Usando regex para encontrar os números entre colchetes
        cycle = IDCycleApost() 
        padrao = r'\[([^]]+)\]'
        lista = re.findall(padrao, texto)
        lista = '\n'.join(lista)
        list = lista.split(',')
        dados_encontrados  = [item.strip().strip("'") for item in list]
        
        dados_encontrados = cycle.transforma_lista(dados_encontrados)
        return dados_encontrados
    
    
    def transforma_lista(self, lista):
        # Inicializa uma lista vazia para armazenar os resultados
        resultado = []

        # Itera sobre os elementos da lista original
        for num in lista:
            # Formata o número como uma string com dois dígitos
            numero_formatado = str(num).zfill(2)
            resultado.append(numero_formatado)

        return resultado
    
    
    def CycleInput(self, results, Cycle):  
        CycleB = []      
        CycleB = Cycle
        for i in results:
            if not i in CycleB:
               Cycle.append(i)
        return Cycle
    
    
cycle = IDCycleApost() 
cycle.AnalityConcurso()