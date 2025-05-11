## install Packgens

## python -m venv .venv

## .\.venv\Scripts\Activate
## python.exe -m pip install --upgrade pip

## pip install pandas
## pip install numpy
 
## pip install tqdm

## pip install loteria-caixa

## pip install rich.progress
## pip install rich

## pip install loteria-caixa tqdm rich.progress rich
## pip install numpy tensorflow scikit-learn


*No PowerShell digitar o comando para desabilitar o Activate.psl
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# -*- coding: utf-8 -*-
from loteria_caixa import MegaSena

concurso = MegaSena()

print(concurso.todosDados())
print(concurso.tipoJogo())
print(concurso.numero())
print(concurso.nomeMunicipioUFSorteio())
print(concurso.dataApuracao())
print(concurso.valorArrecadado())
print(concurso.valorEstimadoProximoConcurso())
print(concurso.valorAcumuladoProximoConcurso())
print(concurso.valorAcumuladoConcursoEspecial())
print(concurso.valorAcumuladoConcurso_0_5())
print(concurso.acumulado())
print(concurso.indicadorConcursoEspecial())
print(concurso.dezenasSorteadasOrdemSorteio())
print(concurso.listaResultadoEquipeEsportiva())
print(concurso.numeroJogo())
print(concurso.nomeTimeCoracaoMesSorte())
print(concurso.tipoPublicacao())
print(concurso.observacao())
print(concurso.localSorteio())
print(concurso.dataProximoConcurso())
print(concurso.numeroConcursoAnterior())
print(concurso.numeroConcursoProximo())
print(concurso.valorTotalPremioFaixaUm())
print(concurso.numeroConcursoFinal_0_5())
print(concurso.listaMunicipioUFGanhadores())
print(concurso.listaRateioPremio())
print(concurso.listaDezenas())
print(concurso.listaDezenasSegundoSorteio())
print(concurso.id())

## git status
## git add .
## git commit -m 'TwoUpApp'
## git push AppApost master


## Criar Um Menu Top ----------------------------------------------------------------

import ClearScren
from colorama import Back, Fore, Style, init

def AnalisesApp():
    ClearScren.cls()
    while True:
        process = input(Fore.YELLOW +
        "--------------------------------\n"
        "|###  Menu Aportes - Budget  ##|\n"
        "| 1 -                          |\n"
        "| 2 -                          |\n"
        "| 3 -                          |\n"
        "| 4 -                          |\n"
        "| 5 -                          |\n"
        "| 6 -                          |\n"
        "| 7 -                          |\n"
        "| 8 -                          |\n"
        "| 9 -                          |\n"
        "| 0 - Sair :                   |\n"
        "--------------------------------\n"
        "==>> ")
        if process == '':
            process = 0                   

        if process == '1' or process == 'Aposta':
           
        elif process == '2' or process == 'Resultados': 
           
        elif process == '3' or process == 'Consulta': 
           
        elif process == '4' or process == 'ApostaEspelho': 
           
        elif process == '5' or process == 'ApostaQuinaFive':
           
        elif process == '6' or process == 'Ultimo_Registro':
            
        elif process == '7' or process == 'Cunsultar_resultados':     
           
        elif process == '8' or process == 'Analisar_Concurso':    
           
        elif process == '9' or process == 'UP_Biblioteca':
           
        elif process == 0 or process == '0':
            ClearScren.cls()
            break    
        else:
            print("Você deve informar um processo validao!")   

## Final do Menu Top ----------------------------------------------------------------            

https://www.usandopy.com/pt/artigo/como-criar-aplicativo-de-controle-de-despesas-pessoais-com-graficos-em-python/#google_vignette
https://www.mazusoft.com.br/lotofacil/tabela-ciclos.php


## *** Criar Deplay de Aplicação 
==>> pip install auto-py-to-exe
## auto-py-to-exe

## ----------------------------------------------------------------------------------------------------------------------------------------------------------------------##
Como usar o machine learning para aumentar suas chances na Lotofácil
Métodos de Machine Learning para Aumentar Suas Chances na Lotofácil.

Métodos de Machine Learning para Aumentar Suas Chances na Lotofácil
Introdução
O machine learning tem se mostrado uma ferramenta poderosa quando aplicada à Lotofácil. Com a capacidade de aprendizado automático dos algoritmos de machine learning, é possível analisar grandes quantidades de dados históricos da Lotofácil e identificar padrões e tendências que podem aumentar suas chances de ganhar. Neste artigo, exploraremos alguns métodos de machine learning que podem ser aplicados para aprimorar suas estratégias na Lotofácil e maximizar suas chances de sucesso.

## Algoritmo de regressão
Um dos métodos mais comuns de machine learning aplicados à Lotofácil é o algoritmo de regressão. Esse algoritmo é capaz de analisar os dados históricos dos sorteios e identificar quais variáveis têm maior influência nos resultados. Por exemplo, ele pode identificar se determinados números tendem a sair com mais frequência ou se existem combinações específicas de números que têm maior probabilidade de serem sorteadas. Com essas informações, é possível selecionar os números com maior probabilidade de serem sorteados, aumentando assim suas chances de acertar os resultados.

## Algoritmo de classificação
Outro método interessante é o algoritmo de classificação. Esse tipo de algoritmo é capaz de categorizar os números de acordo com suas características e analisar quais categorias têm maior probabilidade de serem sorteadas. Por exemplo, ele pode classificar os números em pares e ímpares ou em números baixos e altos. Com base nessa classificação, é possível identificar quais categorias têm maior probabilidade de serem sorteadas e incluir mais números dessa categoria em suas apostas.

Data Science
Aprenda a estatística por trás dos modelos de ML e IA, realize análises exploratórias, treine e teste modelos clássicos e redes neurais, tudo isso com Numpy, Pandas, Scikit-Learn, PyTorch e mais ferramentas Python.
Entre na Lista de Espera
Nossa metodologia de ensino tem eficiência comprovada
Curso da Awari em Data Science
15h de carga horária
2 semanas de duração
Certificado de conclusão
Mentorias individuais

## Algoritmo de agrupamento
Além dos algoritmos de regressão e classificação, também é possível utilizar algoritmos de agrupamento para agrupar os números sorteados em clusters com características semelhantes. Isso pode ajudar a identificar padrões e tendências nos resultados da Lotofácil. Por exemplo, pode-se identificar que determinados clusters de números têm maior probabilidade de serem sorteados juntos ou que determinados clusters têm maior probabilidade de serem sorteados em determinadas posições. Com base nessas informações, é possível selecionar os números que pertencem aos clusters com maior probabilidade de sucesso.

## Utilizando Machine Learning para Melhorar suas Apostas
A aplicação de algoritmos de machine learning na Lotofácil pode fornecer uma vantagem significativa na hora de fazer suas apostas. No entanto, é importante ressaltar que o machine learning não garante uma vitória certa, mas sim aumenta suas chances de sucesso. Portanto, é essencial utilizar esses algoritmos como uma ferramenta complementar às suas estratégias de jogo.

Ao utilizar algoritmos de regressão, classificação e agrupamento, é necessário ter em mente que os resultados são baseados em probabilidades e estatísticas. Não há uma fórmula mágica para acertar os resultados da Lotofácil, mas essas ferramentas podem ajudá-lo a tomar decisões mais informadas na hora de escolher seus números e aumentar suas chances de obter resultados mais favoráveis.

É importante lembrar também que o machine learning depende da qualidade dos dados fornecidos. Quanto mais informações históricas você tiver, melhores serão as análises realizadas pelos algoritmos. Portanto, é interessante manter um banco de dados atualizado com os resultados passados da Lotofácil para obter resultados mais precisos nas análises de machine learning.

## Implementando o Machine Learning para Aprimorar suas Estratégias
A implementação do machine learning para aprimorar suas estratégias na Lotofácil pode ser realizada de diferentes maneiras. Uma opção é desenvolver seus próprios algoritmos de machine learning ou utilizar bibliotecas de machine learning disponíveis em diferentes linguagens de programação, como Python e R.

Existem várias bibliotecas de machine learning populares que podem ser utilizadas para implementar suas estratégias na Lotofácil. Por exemplo, a biblioteca scikit-learn em Python oferece uma ampla gama de algoritmos e ferramentas para aplicação de machine learning, incluindo regressão, classificação e agrupamento.

Data Science
Aprenda a estatística por trás dos modelos de ML e IA, realize análises exploratórias, treine e teste modelos clássicos e redes neurais, tudo isso com Numpy, Pandas, Scikit-Learn, PyTorch e mais ferramentas Python.
Entre na Lista de Espera
Nossa metodologia de ensino tem eficiência comprovada
Curso da Awari em Data Science
15h de carga horária
2 semanas de duração
Certificado de conclusão
Mentorias individuais
Outra opção é utilizar plataformas de machine learning disponíveis na nuvem, como o Google Cloud Machine Learning Engine ou o Amazon Machine Learning. Essas plataformas oferecem infraestrutura e recursos para implementar e treinar modelos de machine learning com facilidade, sem a necessidade de se preocupar com a parte técnica da implantação.

## Práticas de Machine Learning para Aumentar Suas Probabilidades de Ganhar na Lotofácil
Além de utilizar algoritmos de machine learning, existem outras práticas que podem aumentar suas probabilidades de ganhar na Lotofácil. Aqui estão algumas dicas adicionais para complementar suas estratégias:

Analise os resultados passados: Estudar os resultados anteriores da Lotofácil pode ajudar a identificar padrões e tendências que podem guiar suas escolhas. Observe quais números têm sido sorteados com mais frequência e quais combinações têm sido mais comuns.
Diversifique suas apostas: Em vez de apostar apenas em uma combinação de números, diversifique suas apostas e inclua diferentes combinações. Isso aumenta suas chances de acertar pelo menos uma aposta vencedora.
Utilize números quentes e frios: Os números quentes são aqueles que têm sido sorteados com mais frequência, enquanto os números frios são os menos sorteados. Considere incluir tanto números quentes quanto frios em suas apostas para equilibrar as probabilidades.
Aposte em bolões: Participar de bolões é uma ótima maneira de aumentar suas chances de ganhar na Lotofácil. Ao unir forças com outras pessoas, você pode apostar em mais números e aumentar suas probabilidades de acerto.
No geral, a utilização do machine learning para aumentar suas chances de sucesso na Lotofácil demanda a implementação adequada dos algoritmos, a análise dos resultados passados, a aplicação de práticas complementares e a gestão do seu bankroll. É importante ressaltar que o machine learning não garante uma vitória certa, mas sim fornece informações e insights valiosos que podem auxiliar na tomada de decisões mais informadas.

Ao adotar essa abordagem, lembre-se de que cada escolha de aposta é baseada em probabilidades e estatísticas. Utilize o machine learning como uma ferramenta complementar para aprimorar suas estratégias na Lotofácil, mas esteja ciente de que o fator sorte ainda desempenha um papel importante no jogo.

Experimente essas práticas de machine learning em suas apostas na Lotofácil e acompanhe seus resultados ao longo do tempo. Lembre-se de atualizar constantemente seus dados, ajustar seus modelos e continuar aprimorando suas estratégias. Com dedicação, análise inteligente e a aplicação adequada do machine learning, você pode aumentar suas chances de obter resultados satisfatórios na Lotofácil. Boa sorte!

## Awari – Aprenda Ciência de Dados
A Awari é a melhor plataforma para aprender sobre ciência de dados no Brasil. Aqui você encontra cursos com aulas ao vivo, mentorias individuais com os melhores profissionais do mercado e suporte de carreira personalizado para dar seu próximo passo profissional e aprender habilidades como Data Science, Data Analytics, Machine Learning e mais.

Já pensou em aprender de maneira individualizada com profissionais que atuam em empresas como Nubank, Amazon e Google? Clique aqui para se inscrever na Awari e começar a construir agora mesmo o próximo capítulo da sua carreira em dados.

----------------------------------------------------------------------------------------------------------------------------------------------------------
## Processo Git 

git remote -v

git remote add origin https://ProjectLucLac@dev.azure.com/ProjectLucLac/AppApost/_git/AppApost 
git remote add origin https://github.com/LacLuc/-AppApost.git

      /*
	git remote set-url --add --push origin https://ProjectLucLac@dev.azure.com/ProjectLucLac/AppApost/_git/AppApost
	git remote set-url --add --push origin https://github.com/LacLuc/-AppApost.git

	git remote set-url --add --push gitHub https://github.com/LacLuc/-AppApost.git
      */

## Festch
   https://ProjectLucLac@dev.azure.com/ProjectLucLac/AppApost/_git/AppApost (fetch)
   https://ProjectLucLac@dev.azure.com/ProjectLucLac/AppApost/_git/AppApost (push)

   https://github.com/LacLuc/-AppApost.git (fetch)
   https://github.com/LacLuc/-AppApost.git (push)
## Festch End

Token ==>> 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

git status
git add .
git commit -m "UmNome"
git push --set-upstream origin app-main
git push 
git remote remove origin
