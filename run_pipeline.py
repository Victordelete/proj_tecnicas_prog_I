"""
    Script utilizado para executar o pipeline de processamento
"""

from SCRIPTS.globals import *

########################
print("Inicio pipeline")

if not os.path.exists(DATAFRAME_PATH):
    os.makedirs(DATAFRAME_PATH)

print("Limpeza dos dados")
#chamar o módulo de limpeza dos dados recebidos
df = pd.read_csv(RAW_TABLE, low_memory=False)
df = df.replace(" ",np.nan)
print(df.isna().sum())
print(df.nunique())

print("Processamento dos dados")
#chamar o módulo de processamento

print("Analise dos dados")
#chamar o módulo de analise do dado recebido