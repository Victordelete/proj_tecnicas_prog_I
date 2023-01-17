"""
Script para realizar o processamento dos dados para a staging area
- limpesa de dados nulos. 
- limpesa de linhas duplicadas.
- persistências dos dados na staging area.
"""
import itertools
from SCRIPTS.globals import *

def carrega_do_datalake() -> pd.DataFrame:
    """
    Carrega a base de dados ingerida do datalake.

    Returns
    ''''''''
    pd.DataFrame
        base de dados
    """
    data = pd.read_csv(os.path.join(root_path, datalake_file), oriente='index')

    return data

def tratamento_preliminar(data: pd.DataFrame) -> pd.DataFrame:
    """"
    Realiza o tratamento preliminar dos dados

    Parameter
    '''''''
    data : pd.DataFrame
        dados ingeridos na forma de tabela 

    Returns
    '''''''
    pd.DataFrame
        dados tratados

    #Transformar os dados em lista "corrida"

    """
    return data


################################################

if __name__ == '__main__':

    #carregar os dados do datalake
    data = carrega_do_datalake()

    #processamento preliminar
    data_stg = tratamento_preliminar(data)