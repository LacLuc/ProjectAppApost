import src.services.NewID as NewID 
import re

class SaveFile():
    def SalvarDados(ID, Ref1):
        try:
            with open(f'wdb_MegaSenaIDArkivo.txt', 'a+') as file:      
                file.write(f"{ID}, {Ref1} \n")
                file.seek(0)
        except ValueError:
                    print(f'Existe Um Erro')

        try:      
            with open(f'wdb_MegaSenaArkivo.txt', 'a+') as file:           
                file.write(f"{Ref1} \n")
                file.seek(0)  
        except ValueError:
                print(f'Existe Um Erro')

#--------------------------------------------------
#--------------------------------------------------

    def SalvarDadosMoreResult(ID, Loterias, loterias_jogos):
        try:
            with open(f'wdb_Result_{Loterias}.txt', 'a+') as file:      
                file.write(f"{ID}, {loterias_jogos} \n")
                file.seek(0)
        except ValueError:
                print(f'Existe Um Erro')        
            
#--------------------------------------------------
#--------------------------------------------------

    def SalvarDadosTopFive(ID, Ref1, Ref2, Ref3, Ref4):
        try:
            with open(f'wdb_ApostTopFive.txt', 'a+') as file:      
                file.write(f"{ID}, {Ref1}, {Ref2}, {Ref3}, {Ref4} \n")
                file.seek(0)
        except ValueError:
                print(f'Existe Um Erro')

        try:      
            with open(f'wdb_ArkivotTopFive.txt', 'a+') as file: 
                numbers = re.findall(r'\[(.*?)\]', Ref1)  
                removed_chars = ['.', ',', '!', '[', ']']
                chars = set(removed_chars)        
                s = ''.join(filter(lambda x: x not in chars, numbers))         
                res = re.sub('[.,!]', '', s)
                file.write(f"{res} \n")
                file.seek(0)  
        except ValueError:
                print(f'Existe Um Erro')

#--------------------------------------------------
#--------------------------------------------------

    def SalvarBinario(Ref1, Ref2):
        try:
            with open(f'wdb_Binario{Ref2}Arkivo.txt', 'a+') as file:      
                file.write(f"{Ref1}\n")
                file.seek(0)
        except ValueError:
                    print(f'Existe Um Erro')    

#--------------------------------------------------
#--------------------------------------------------
    def SeveDados(ID, Ref1):
        try:
            with open(f'wdb_ProbAllArkivo.txt', 'a+') as file:      
                file.write(f"{Ref1} \n")
                file.seek(0)
        except ValueError:
                    print(f'Existe Um Erro')
#--------------------------------------------------
#--------------------------------------------------
    def SeveCycle(Ref1):
        try:
            with open(f'wdb_ProCycle.txt', 'a+') as file:      
                file.write(f"{Ref1} \n")
                file.seek(0)
        except ValueError:
                    print(f'Existe Um Erro')                 
#--------------------------------------------------
#--------------------------------------------------
    def SeveAllResult(Ref1):
        try:
            with open(f'wdb_ProbAllResult.txt', 'a+') as file:      
                file.write(f"{Ref1} \n")
                file.seek(0)
        except ValueError:
                    print(f'Existe Um Erro')

#--------------------------------------------------
#--------------------------------------------------
    def modify_record(target_record, new_value):
        try:
            with open(f'wdb_ProbAllResult.txt', 'r+') as file:
                lines = file.readlines()
                for i, line in enumerate(lines):
                    id = int(SaveFile.OUCs(line, 'Ult_Concurso'))
                    if target_record == id  :
                        lines[i] = str(new_value) + '\n'
                        break  # Encerra a busca após encontrar o registro
                file.seek(0)
                file.writelines(lines)
        except FileNotFoundError:
            print(f"O arquivo não foi encontrado.")
            try:
                with open(f'wdb_ProbAllResult.txt', 'a+') as file:      
                    file.write(f"{new_value} \n")
                    file.seek(0)
            except ValueError:
                    print(f'Existe Um Erro')

#--------------------------------------------------
#--------------------------------------------------
    def OUCs(dados,Regist):
        if dados != '\n':    
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
#--------------------------------------------------
#--------------------------------------------------

    def SalvarFiles(ID, Ref1, Ref2, Ref3, Ref4):
        try:
            with open(f'wdb_ApostTopFive.txt', 'a+') as file:      
                file.write(f"{ID}, {Ref1}, {Ref2}, {Ref3}, {Ref4} \n")
                file.seek(0)
        except ValueError:
                print(f'Existe Um Erro')

        try:      
            with open(f'wdb_ArkivotTopFive.txt', 'a+') as file: 
                numbers = re.findall(r'\[(.*?)\]', Ref1)  
                removed_chars = ['.', ',', '!', '[', ']']
                chars = set(removed_chars)        
                s = ''.join(filter(lambda x: x not in chars, numbers))         
                res = re.sub('[.,!]', '', s)
                file.write(f"{res} \n")
                file.seek(0)  
        except ValueError:
                print(f'Existe Um Erro')

#--------------------------------------------------
#--------------------------------------------------

    def SalvarDadosFilas(ID, Ref1):
        try:
            with open(f'wdb_MegaSenaIDArkivo.txt', 'a+') as file:      
                file.write(f"{ID}, {Ref1} \n")
                file.seek(0)
        except ValueError:
                    print(f'Existe Um Erro')

        try:      
            with open(f'wdb_MegaSenaArkivo.txt', 'a+') as file:           
                file.write(f"{Ref1} \n")
                file.seek(0)  
        except ValueError:
                print(f'Existe Um Erro')        

#--------------------------------------------------
#--------------------------------------------------

    def SalvarMoreResult(ID, Loterias, loterias_jogos):
        try:
            with open(f'wdb_Result_{Loterias}.txt', 'a+') as file:      
                file.write(f"{ID}, {loterias_jogos} \n")
                file.seek(0)
        except ValueError:
                print(f'Existe Um Erro')

#--------------------------------------------------
#--------------------------------------------------

    def SalvarTopFive(ID, Ref1, Ref2, Ref3, Ref4):
        try:
            with open(f'wdb_ApostTopFive.txt', 'a+') as file:      
                file.write(f"{ID}, {Ref1}, {Ref2}, {Ref3}, {Ref4} \n")
                file.seek(0)
        except ValueError:
                print(f'Existe Um Erro')

        try:      
            with open(f'wdb_ArkivotTopFive.txt', 'a+') as file: 
                numbers = re.findall(r'\[(.*?)\]', Ref1)  
                removed_chars = ['.', ',', '!', '[', ']']
                chars = set(removed_chars)        
                s = ''.join(filter(lambda x: x not in chars, numbers))         
                res = re.sub('[.,!]', '', s)
                file.write(f"{res} \n")
                file.seek(0)  
        except ValueError:
                print(f'Existe Um Erro')
        