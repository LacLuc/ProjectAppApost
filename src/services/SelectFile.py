import NewID as re

class SelectFile():
    def ReadFile(string_input):
        with open(f'wdb_{string_input}.txt', 'r', encoding='utf-8') as file:
            content = file.readlines()
        return content    
    

    def ReadFileResult(string_input):
        with open(f'wdb_Result_{string_input}.txt', 'r', encoding='utf-8') as file:
            content = file.readlines()
        return content  


    def selectDados():
        try:
            with open(f'wdb_ProbAllArkivo.txt', 'r', encoding='utf-8') as file:
                content = file.readlines()
            return content
        except ValueError:
                        print(f'Existe Um Erro')

    def selectCycle():
        try:
            with open(f'wdb_ProCycle.txt', 'r', encoding='utf-8') as file:
                content = file.readlines()
            return content
        except ValueError:
                        print(f'Existe Um Erro')

    def selectProbAllResult():
        try:
            with open(f'wdb_ProbAllResult.txt', 'r', encoding='utf-8') as file:
                content = file.readlines()
            return content
        except ValueError:
                        print(f'Existe Um Erro')



    '''
    def Count_Num(string_input):
        with open(f'{string_input}.txt', 'r') as file:
            y = 1
            x = len(file.readlines())
            while y >= x:
                content = file.readlines()
                numbers = re.findall(r'\[(.*?)\]', content)
                removed_chars = ['.', ',', '!', '[', ']']
                chars = set(removed_chars)        
                s = ''.join(filter(lambda x: x not in chars, numbers))         
                res = re.sub('[.,!]', '', s)
                print(res)
                y +=1       

    Count_Num(input('Digite o Arquivo: '))
    '''    