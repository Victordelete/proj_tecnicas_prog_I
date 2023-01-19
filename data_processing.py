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
def criar_tabela_silver() -> pd.DataFrame:
    colunas_mantidas = ["FID", "ADDRESBR", "CBSANAMB", "CITYBR", "CNTRYNAB", "DEPSUMBR", "NAMEBR", "ADDRESS", "BKCLASS", "CITY", "CNTRYNA", "DEPDOM", "SCORE", "NAMEFULL", "STNAMEBR", "STALPBR", "ASSET"]
    df_silver_seguro_depositos_federais = pd.read_csv(ROOT_PATH + r"\dataset_kaggle.com\b_seguro_depositos_federais.csv")
    for coluna_tabela in df_silver_seguro_depositos_federais.columns.values:
        if coluna_tabela not in colunas_mantidas:
            df_silver_seguro_depositos_federais = df_silver_seguro_depositos_federais.drop(columns=coluna_tabela)

    df_silver_seguro_depositos_federais.to_csv(ROOT_PATH + r"\dataset_kaggle.com\s_seguro_depositos_federais.csv")
    

################################################

if __name__ == '__main__':
    criar_tabela_silver()
    print(f'{dt.now()} [INFO] Dados processados com sucesso.')