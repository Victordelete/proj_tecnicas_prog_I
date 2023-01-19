"""
    Script utilizado para executar o pipeline de processamento
"""

from globals import *

#########################
#INSERCAO DOS DADOS DISPONIVEIS
print(f'{dt.now()} [INFO] Iniciando ingestão dos dados.')
os.system('python "' + os.path.join(root_path, data_ingestion) + '"')

#########################
#PROCESSAMENTO DOS DADOS
print(f'{dt.now()} [INFO] Iniciando processamento dos dados.')
os.system('python "' + os.path.join(root_path, data_processing) + '"')

#########################
#DATALAKE
print(f'{dt.now()} [INFO] Iniciando atualização do datalake.')

#########################
#VISUALIZAÇÃO DOS DADOS
print(f'{dt.now()} [INFO] Iniciando criação de visualização dos dados.')