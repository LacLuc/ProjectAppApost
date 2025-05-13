# -*- coding: utf-8 -*-

from loteria_caixa import *
#(MegaSena, LotoFacil, Quina, LotoMania, TimeMania,
# DuplaSena, Federal, Loteca, DiadeSorte, SuperSet)

def ResultApost(Loterias,jogo):
    try:
        concurso = Result_func(Loterias, jogo)
        return  concurso.numero(), concurso.dataApuracao(), concurso.listaDezenas() 
    except ValueError:
        print(f'Existe Um Erro de Connection! ')

def ResultDelta(Loterias,jogo):
    try:
        concurso = Result_func(Loterias, jogo)
        return  concurso
    except ValueError:
        print(f'Existe Um Erro de Connection! ')

def UltmResult(Loterias):
    try:
        if Loterias == 'MegaSena':
            concurso = MegaSena()
        elif Loterias == 'LotoFacil':
            concurso = LotoFacil()
        elif Loterias == 'Quina':
            concurso = Quina()
        elif Loterias == 'LotoMania':
            concurso = LotoMania()
        elif Loterias == 'TimeMania':
            concurso = TimeMania()
        elif Loterias == 'DuplaSena':
            concurso = DuplaSena()
        elif Loterias == 'Federal':
            concurso = Federal()
        elif Loterias == 'Loteca':
            concurso = Loteca()  
        elif Loterias == 'DiadeSorte':
            concurso = DiadeSorte()
        elif Loterias == 'SuperSet':
            concurso = SuperSet()
        else:
            concurso = f'Loteria Not Existe {Loterias}'
        return concurso 
    except ValueError:
        print(f'Existe Um Erro de Connection! ')


def get_numero(Loterias,jogo):
    try:
        concurso = Result_func(Loterias, jogo)       
        register = concurso.numero()
        return register
    except ValueError:
        print(f'Existe Um Erro de Connection! ')


def Result_func(Loterias, jogo):
    try:
        if Loterias == 'MegaSena':
            concurso = MegaSena(jogo)
        elif Loterias == 'LotoFacil':
            concurso = LotoFacil(jogo)  
        elif Loterias == 'Quina':
            concurso = Quina(jogo)         
        elif Loterias == 'LotoMania':
            concurso = LotoMania(jogo)
        elif Loterias == 'TimeMania':
            concurso = TimeMania(jogo)
        elif Loterias == 'DuplaSena':
            concurso = DuplaSena(jogo)
        elif Loterias == 'Federal':
            concurso = Federal(jogo)
        elif Loterias == 'Loteca':
            concurso = Loteca(jogo)
        elif Loterias == 'DiadeSorte':
            concurso = DiadeSorte(jogo)
        elif Loterias == 'SuperSet':
            concurso = SuperSet(jogo)
        return concurso  
    except ValueError:
        print(f'Existe Um Erro de Connection! ')          


    ''' Todos os doc ## https://pypi.org/project/loteria-caixa/...

    pip install loteria-caixa

    loteria-caixa 0.0.5

    Abaixo todos os comandos

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
            
    '''



