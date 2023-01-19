from globals import *

WEB_TABLE_FILE = ROOT_PATH + r"\dataset_kaggle.com\s_seguro_depositos_federais.csv"
data = pd.read_csv(WEB_TABLE_FILE , low_memory=False)

print(data.head())