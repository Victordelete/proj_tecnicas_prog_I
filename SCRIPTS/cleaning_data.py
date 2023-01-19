""""
Script para limpeza dos dados analisados.
"""

from globals import *

def limpar_nulos(df):
    df = pd.read_csv(RAW_TABLE, low_memory=False)
    df = df.replace(" ",np.nan)
    print(df.isna().sum())


##########################

if __name__ == '__main__':
    limpar_nulos()