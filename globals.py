"""
    Script de configuração geral
"""

import os
import numpy as np
import pandas as pd
from datetime import datetime as dt

###############################################
#definições gerais
root_path = os.path.dirname((os.path.realpath(__file__)))


###############################################
#definições - sistema de ingestão 
data_ingestion = "data_ingestion.py"
data_ingestion_file = "dataset_kaggle.com\data_ingestion_file.csv"


###############################################
#processamento de dados
data_processing = "data_processing.py"


###############################################
#dados de origem
datalake_file = "dataset_kaggle.com\Federal_Deposit_Insurance_Corporation_FDIC_Insured_Banks.csv"


###############################################
#definições - staging area
staging_data = 'dataset_kaggle.com\staging_data.csv'
