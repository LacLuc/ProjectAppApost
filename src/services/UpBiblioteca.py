import subprocess
import sys

def verificar_atualizacao(nome_pacote):
    # Verifica a versão instalada do pacote
    versao_instalada = subprocess.run([sys.executable, '-m', 'pip', 'show', nome_pacote], capture_output=True, text=True)
    versao_instalada = versao_instalada.stdout.split('Version: ')[1].split('\n')[0]

    # Verifica a versão mais recente disponível no PyPI
    versao_disponivel = subprocess.run([sys.executable, '-m', 'pip', 'index', 'versions', nome_pacote], capture_output=True, text=True)
    versao_disponivel = versao_disponivel.stdout.split('Available versions: ')[1].split('\n')[0].split(' ')[0]

    # Compara as versões e atualiza se necessário
    if versao_instalada != versao_disponivel:
        print(f'Atualizando {nome_pacote} da versão {versao_instalada} para {versao_disponivel}...')
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', nome_pacote])
        print(f'{nome_pacote} atualizado com sucesso.')
    else:
        print(f'{nome_pacote} já está na versão mais recente ({versao_instalada}).')

