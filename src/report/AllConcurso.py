import re
import src.services.ClearScren as ClearScren
import src.controller.ConsultOne as ConsultOne
import src.services.Hour as Hour
import src.model.MsgAnalityArkivo as Msg
import src.services.ConverterBase as Conv
import src.services.SelectFile as dba
import src.services.SaveFile as dbb
import AnalityArkivo as Aty
import ValidarResult as vR

class IDValidator:
    def __init__(self):
        self.probaby = set()  # Tabela nº1 com 3 milhões de registros
        self.content = set()  # Tabela nº2 com itens registrados da tabela nº1
        self.probblt = set()  # Tabela nº3 com 2000 registros

    def AnalityConcurso(self):
        ClearScren.cls()
        print('-='*5,' Analises_Concurso ', '=-'*5)
        Loterias = ConsultOne.MsgJogos()
        if Loterias == "LotoFacil":
            validator = IDValidator()
            validator.NumberCount(Loterias)
        else:
            print("Apenas a Loto esta cadastrada!")

    def NumberCount(self,string_input):                
        ClearScren.cls() 
        try:
            validator = IDValidator()           
            validator.load_data(string_input)  
            validator.validate_and_register()              
            Hour.horario()        
        except ValueError:
            print(f'Existe Um Erro')


    def load_data(self, string_input):
        """Carrega os dados nas tabelas nº1 e nº3."""     
        validator = IDValidator() 
        self.probaby = dba.SelectFile.selectDados()
        self.content = dba.SelectFile.ReadFileResult(string_input)
        self.probblt = dba.SelectFile.selectProbAllResult()


    def validate_and_register(self):
        """Valida e registra um ID na tabela content."""
        validator = IDValidator()

        print('-='*5,' Confere Tabela com 3 Milhões de Registros ', '=-'*5)        
        listprobaby = Aty.QProcessRun()
        listprobaby.sort()  
        probaby = validator.registroVld(self.probaby, listprobaby)
        
        
        print('-='*5,' Analisar_Concurso_Resultados ', '=-'*5)
        listConcurso = Aty.QProcessRun()
        listConcurso.sort()    
        contesto = validator.registroVld(self.content, listConcurso)
        Hour.horario()
                
        for prb in probaby:      # Tabela nº1 com 3 milhões de registros
            for con in contesto:    
                self.probblt = dba.SelectFile.selectProbAllResult()  
                #for pb in self.probblt: # content com registrados da probaby                    
                h = validator.verificarProCon(con, prb, self.probblt)
                if h == 'erro':
                   break


    def verificarProCon(self, con, prb, probblt):
        validator = IDValidator()

        results = validator.extrair_dados(con)       # Apenas os numeros do Resultado
        Id_Result = Aty.Validationfind(con)          # Apenas o ID do Resultado
        proby = validator.extrair_dados(prb)         # Apenas os numeros da aposta            
        Id_Apost = int(validator.OUC(prb, 'Aposta')) # Apenas o Id da aposta

        con = validator.probbltVld(probblt, Id_Apost)
        if con == 0:
            registroOK = 0
        else:    
            for Vlb in con:
                pb = Vlb
            registroOK = validator.Registred(Id_Result,Id_Apost,pb)

        if registroOK == 1:        
            Qtde = validator.Vldar(Id_Result, proby, results, Id_Apost, pb)    
        if registroOK == 0:
            refPass = ''
            Qtde = validator.Vldar(Id_Result, proby, results, Id_Apost, refPass)
            return ''
        if registroOK == 2:
            return ''
        Qtde = ''    
        return Qtde
    

    def extrair_dados(self, texto):
        # Usando regex para encontrar os números entre colchetes
        validator = IDValidator()
        padrao = r'\[([^]]+)\]'
        lista = re.findall(padrao, texto)
        lista = '\n'.join(lista)
        list = lista.split(',')
        dados_encontrados  = [item.strip().strip("'") for item in list]
        
        dados_encontrados = validator.transforma_lista(dados_encontrados)
        return dados_encontrados


    def Registred(self, Id_Result, Id_Apost, pb):   
        validator = IDValidator() 
        try:
            id_concurso = int(validator.OUC(pb, 'Ult_Concurso'))
            id_aposta = int(validator.OUC(pb, 'Aposta'))
            if id_concurso == Id_Apost:
                if id_aposta >= Id_Result:
                    return 2
                else:
                    return 1
            else:
                return 0
        except FileNotFoundError:
            return 0
        

    def registroVld(self, content, listConcurso):
        validator = IDValidator() 
        listas = []
        Qtde = 0
        for con in content:
            Id_Nro = Aty.Validationfind(con)
            if Id_Nro is None:
                Id_Nro = int(validator.OUC(con, 'Aposta'))

            if Id_Nro in listConcurso:
                listas.append(con)
                Qtde += 1
            if Qtde == len(listConcurso):
                return listas
        return listas
    

    def probbltVld(self, probblt, Id_Apost):
        validator = IDValidator() 
        listas = []
        for con in probblt:
            Id_Nro = int(validator.OUC(con, 'Ult_Concurso'))
            if Id_Nro == Id_Apost:
                listas.append(con)       
                return listas
        return 0
    

    def transforma_lista(self, lista):
        # Inicializa uma lista vazia para armazenar os resultados
        resultado = []

        # Itera sobre os elementos da lista original
        for num in lista:
            # Formata o número como uma string com dois dígitos
            numero_formatado = str(num).zfill(2)
            resultado.append(numero_formatado)

        return resultado
    

    def Vldar(self, Id_Nro, prb, results, NroApost, refPass):
        validator = IDValidator()
        if refPass == '':
            probblt = dba.SelectFile.selectProbAllResult()
            for pb in probblt:
                try:
                    id = validator.OUC(pb, 'Ult_Concurso')
                except FileNotFoundError:
                    sttus = 0
                    break

                if NroApost == int(id):
                    sttus = 1
                    break
                else:
                    sttus = 0
                    break
            sttus = 0
        else:
            pb = refPass 
            NroApost = int(validator.OUC(refPass, 'Ult_Concurso'))   
            sttus = 1

        validar = vR.conferir_aposta_lotofacil(results, prb)   
        if sttus == 1:
            updateArkivo = 1
            if len(validar) == 11:
                A_11 = int(validator.OUC(pb, 'Acerto_11')) + 1
            else:
                A_11 = int(validator.OUC(pb, 'Acerto_11'))
            if len(validar) == 12:    
                A_12 = int(validator.OUC(pb, 'Acerto_12')) + 1
            else:
                A_12 = int(validator.OUC(pb, 'Acerto_12'))
            if len(validar) == 13:
                A_13 = int(validator.OUC(pb, 'Acerto_13')) + 1
            else:
                A_13 = int(validator.OUC(pb, 'Acerto_13'))
            if len(validar) == 14:
                A_14 = int(validator.OUC(pb, 'Acerto_14')) + 1   
            else:
                A_14 = int(validator.OUC(pb, 'Acerto_14'))
            if len(validar) == 15:   
                A_15 = int(validator.OUC(pb, 'Acerto_15')) + 1
            else:
                A_15 = int(validator.OUC(pb, 'Acerto_15'))
            game = prb
        else:     
            updateArkivo = 0       
            A_11, A_12, A_13, A_14, A_15 = 0, 0, 0, 0, 0
            if len(validar) == 11:
                A_11 =+ 1
            elif len(validar) == 12:    
                A_12 =+ 1
            elif len(validar) == 13:
                A_13 =+ 1
            elif len(validar) == 14:
                A_14 =+ 1        
            elif len(validar) == 15:   
                A_15 =+ 1
            game = prb

        meu_dicionario = {
            "Ult_Concurso": str(NroApost).zfill(7),
            "Aposta": Id_Nro,
            "Acerto_11": A_11,
            "Acerto_12": A_12,
            "Acerto_13": A_13,
            "Acerto_14": A_14,
            "Acerto_15": A_15,
            "Jogo_All": game
        }        
        validator.VldAndUpdate(updateArkivo, NroApost, meu_dicionario)


    def VldAndUpdate(self, updateArkivo, NroApost, meu_dicionario):    
        # Exemplo de uso:
        validator = IDValidator()
        meu_dicionario = validator.ReMooV(meu_dicionario)
        if updateArkivo == 1:
            dbb.SaveFile.modify_record(NroApost, meu_dicionario)
        else:
            dbb.SaveFile.SeveAllResult(meu_dicionario)  
            print(meu_dicionario)


    def ReMooV(self, meu_dicionario):
        if "\n" in meu_dicionario:
            dados_limpos = meu_dicionario.strip("\n")
            return dados_limpos
        else:
            return meu_dicionario
            
    
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


#//--Inicia o Modulo ------------------------//
#//------------------------------------------//

#validator = IDValidator()
#validator.AnalityConcurso()