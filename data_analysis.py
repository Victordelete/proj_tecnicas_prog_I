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
    colunas_mantidas = [ "STNAMEBR"]
    data = pd.read_csv(ROOT_PATH + r"\dataset_kaggle.com\s_seguro_depositos_federais.csv")
    for coluna_tabela in data.columns.values:
        if coluna_tabela not in colunas_mantidas:
            data = data.drop(columns=coluna_tabela)
    data = data.groupby("STNAMEBR").size()
    data.sort_values(ascending=False, inplace=True)
    data.to_csv(ROOT_PATH + r"\dataset_kaggle.com\visao_por_estado.csv")
    
def participacao_mercado() ->pd.DataFrame:
    data = pd.read_csv(DATALAKE_FILE, low_memory=False)

    # Agrupando os bancos pelo nome, utilizando a coluna NAMEFULL
    agrupando_bancos = data.groupby("NAMEFULL").size()

    # Calculando a participação de mercado de cada banco
    participacao_individual = agrupando_bancos / len(data) * 100

    # Ordenando os resultados pelo maior valor de participação de mercado
    participacao_individual.sort_values(ascending=False, inplace=True)

    # A variável participacao_individual possui a lista completa de todos os bancos
    # utilizando len(participacao_individual) é possível verificar que há 5746 registros
    # Para facilitar a visualização trabalharemos com os 15 bancos com mais participação de mercado

    # Selecionando os 15 bancos com mais participação de mercado
    top_15 = participacao_individual.head(15)
    top_15.to_csv(ROOT_PATH + r"\dataset_kaggle.com\participacao_mercado.csv")


################################################

if __name__ == '__main__':
    criar_tabela_score_bancos_porto_rico()
    visao_por_estado()
    participacao_mercado()
    print(f'{dt.now()} [INFO] Finalizado a analise com sucesso.')