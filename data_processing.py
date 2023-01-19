"""
Script para realizar o processamento dos dados para a staging area
- limpesa de dados nulos. 
- limpesa de linhas duplicadas.
- persistências dos dados na staging area.
"""
import itertools
from globals import *

#########################
#funcoes de limpeza de dados
def limpa_dados() -> pd.DataFrame:
    df = pd.read_csv(DATALAKE_FILE, low_memory=False)
    df = df.replace(" ",np.nan)
    return df


################################################

if __name__ == '__main__':

    data = limpa_dados()
    print(data.head())