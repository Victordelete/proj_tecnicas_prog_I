"""
    Script utilizado para executar o pipeline de processamento
"""

from SCRIPTS.globals import *

########################
print("Inicio pipeline")

print("Limpeza dos dados")
#chamar o módulo de limpeza dos dados recebidos
df = pd.read_csv(datalake_file, low_memory=False)
df = df.replace(" ",np.nan)
print(df.isna().sum())


print("Processamento dos dados")
#chamar o módulo de processamento

print("Analise dos dados")
#chamar o módulo de analise do dado recebido