"""
Algoritmo para inserção de dados por meio do arquivo de insercao
"""

from globals import *

def inserir_dados_camada_bronze():
    WEB_TABLE_FILE = ROOT_PATH + r"\dataset_kaggle.com\Federal_Deposit_Insurance_Corporation_FDIC_Insured_Banks.csv"
    df_seguro_depositos_federais = pd.read_csv(WEB_TABLE_FILE, low_memory=False)
    df_seguro_depositos_federais = df_seguro_depositos_federais.replace(" ",np.nan)
    df_seguro_depositos_federais.to_csv(ROOT_PATH + r"\dataset_kaggle.com\b_seguro_depositos_federais.csv")


if __name__ == '__main__':
    inserir_dados_camada_bronze()
    print(f'{dt.now()} [INFO] Dados inseridos com sucesso.')
    
    