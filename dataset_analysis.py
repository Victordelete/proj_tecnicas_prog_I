from globals import *

#########################
#funcoes para extrair um valor e visão de negocio
def criar_tabela_score_bancos_porto_rico() -> pd.DataFrame:
    colunas_mantidas = ["SCORE", "CNTRYNAB", "NAMEFULL"]
    criar_tabela_score_bancos_porto_rico = pd.read_csv(ROOT_PATH + r"\dataset_kaggle.com\s_seguro_depositos_federais.csv")
    for coluna_tabela in criar_tabela_score_bancos_porto_rico.columns.values:
        if coluna_tabela not in colunas_mantidas:
            criar_tabela_score_bancos_porto_rico = criar_tabela_score_bancos_porto_rico.drop(columns=coluna_tabela)

    criar_tabela_score_bancos_porto_rico = criar_tabela_score_bancos_porto_rico.loc[(criar_tabela_score_bancos_porto_rico.CNTRYNAB == "Puerto Rico")]
    criar_tabela_score_bancos_porto_rico = criar_tabela_score_bancos_porto_rico.groupby("NAMEFULL").mean().sort_values(by=["SCORE"],ascending=False).reset_index()

    criar_tabela_score_bancos_porto_rico.to_csv(ROOT_PATH + r"\dataset_kaggle.com\g_score_bancos_porto_rico.csv")
    
def visao_por_estado() -> pd.DataFrame:
    colunas_mantidas = ["CNTRYNAB", "STNAMEBR"]
    data = pd.read_csv(ROOT_PATH + r"\dataset_kaggle.com\s_seguro_depositos_federais.csv")
    for coluna_tabela in data.columns.values:
        if coluna_tabela not in colunas_mantidas:
            data = data.drop(columns=coluna_tabela)
    data.to_csv(ROOT_PATH + r"\dataset_kaggle.com\visao_por_estado.csv")
    


################################################

if __name__ == '__main__':
    criar_tabela_score_bancos_porto_rico()
    visao_por_estado()
    print(f'{dt.now()} [INFO] Finalizado a analise com sucesso.')