"""
    Script utilizado para executar o pipeline de processamento
"""

from globals import *

#########################
#INSERCAO DOS DADOS DISPONIVEIS
print(f'{dt.now()} [INFO] Iniciando ingestão dos dados.')
os.system('python "' + os.path.join(ROOT_PATH, DATA_INGESTION_FILE_NAME) + '"')

#########################
#PROCESSAMENTO DOS DADOS
print(f'{dt.now()} [INFO] Iniciando processamento dos dados.')
os.system('python "' + os.path.join(ROOT_PATH, DATA_PROCESSING) + '"')

#########################
#ANALISE DOS DADOS
print(f'{dt.now()} [INFO] Iniciando processamento dos dados.')
os.system('python "' + os.path.join(ROOT_PATH, DATA_ANALYSIS) + '"')

#########################
#APRESENTACAO
print(f'{dt.now()} [INFO] Iniciando apresentacao da analise.')
#os.system('python "' + os.path.join(ROOT_PATH, DATA_APRESENTATION) + '"')
os.system('jupyter notebook "' + os.path.join(ROOT_PATH, DATA_APRESENTATION) + '"')
