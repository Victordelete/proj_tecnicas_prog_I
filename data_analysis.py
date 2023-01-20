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
    criar_tabela_score_bancos_porto_rico = criar_tabela_score_bancos_porto_rico[criar_tabela_score_bancos_porto_rico.NAMEFULL != "Banesco USA"]
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

def ativos_bancos_estado() -> pd.DataFrame:
    # Verificado que no dataset existem alguns países e ilhas agregadas aos EUA como, por exemplo, 
    # A'merican Samoa e Marshall Islands
    # Para uma análise mais precisa utilizaremos somente os 50 estados oficiais pertencentes aos EUA

    # Primeiramente utilizando a biblioteca 'us' disponível em https://pypi.org/project/us/ para criar uma lista de todos os estados

    ''' Código para importas dados da biblioteca US
    from us import states
    estados_oficiais = [state.name for state in states.STATES]    
    '''
   
    # Limpando o DataFrame, utilizando os dados de 'STNAMEBR' que estão em 'estados_oficiais'
    data = pd.read_csv(DATALAKE_FILE, low_memory=False)
    data = data[data['STNAMEBR'].isin(estados_oficiais)]

    # Agrupando os bancos pelo estado, utilizando a coluna STALPBR
    bancos_por_estado = data.groupby('STALPBR')

    # Calcular a média dos ativos de cada estado
    media_por_estado = bancos_por_estado['ASSET'].sum()

    # Juntando 'informcaoes_por_estado' com 'media_por_estado'

    informcaoes_por_estado = data[['STALPBR', 'STNAMEBR']].drop_duplicates()
    media_por_estado = pd.merge(media_por_estado, informcaoes_por_estado, on='STALPBR')

    # Ordenando por ativos 
    media_por_estado = media_por_estado.sort_values(by='ASSET', ascending=False)

    # Criando um gráfico com os dados
    # Para melhor visualização em formato gráfico, utilizamos somente os 15 maiores
    # Exibindo somente os 15 maiores

    top_15_estados = media_por_estado.head(15)
    top_15_estados.to_csv(ROOT_PATH + r"\dataset_kaggle.com\ativos_bancos_estado.csv")

    # Os dados podem ser adquiridos diretamente pela API do bea.gov, mas como são dados simples e 
    # de fácil importação por csv foi optado por esta maneira
    # Carregar os dados e apresentar cabeçalho do df (DataFrame)
    df_gdp = pd.read_csv(ROOT_PATH + r"\dataset_kaggle.com\Gross_Domestic_Product_by_State_2021.csv")

    # Realizando a junção dos dados do dataset estadual com o valor do PIB por estado
    juncao_ativos_com_pib = media_por_estado.merge(df_gdp, left_on='STNAMEBR', right_on='state')

    # Excluindo a coluna 'state' do DataFrame gerado pela união
    juncao_ativos_com_pib = juncao_ativos_com_pib.drop('state', axis=1)

    # Somando valores das colunas Asset e gdp, para calcular o total. Criando as colunas 'ASSET_%' e '2021gdp_%'
    # representam o valor em porcentagem do total para cada estado

    juncao_ativos_com_pib['ASSET_%'] = juncao_ativos_com_pib['ASSET'].div(juncao_ativos_com_pib['ASSET'].sum()) * 100
    juncao_ativos_com_pib['2021gdp_%'] = juncao_ativos_com_pib['2021gdp'].div(juncao_ativos_com_pib['2021gdp'].sum()) * 100

    # Organizando o DataFrame pelo valor do ativo de cada estado

    juncao_ativos_com_pib = juncao_ativos_com_pib.sort_values(by='ASSET', ascending=False)
    juncao_ativos_com_pib.to_csv(ROOT_PATH + r"\dataset_kaggle.com\ativos_bancos_pib_estado.csv")
    ################################################

if __name__ == '__main__':
    criar_tabela_score_bancos_porto_rico()
    visao_por_estado()
    participacao_mercado()
    ativos_bancos_estado()
    print(f'{dt.now()} [INFO] Finalizado a analise com sucesso.')