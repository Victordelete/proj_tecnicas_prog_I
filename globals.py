"""
    Script de configuração geral
"""

import os
import numpy as np
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime as dt

###############################################
#definições gerais
ROOT_PATH = os.path.dirname((os.path.realpath(__file__)))

###############################################
#definições - sistema de ingestão 
DATA_INGESTION_FILE_NAME = "data_ingestion.py"
DATA_INGESTION_FILEPATH = ROOT_PATH + r"\dataset_kaggle.com\data_ingestion_file.csv"
BRONZE_TABLE_FILEPATH = ROOT_PATH + r"\dataset_kaggle.com\b_seguro_depositos_federais.csv"
SILVER_TABLE_FILEPATH = ROOT_PATH + r"\dataset_kaggle.com\s_seguro_depositos_federais.csv"

###############################################
#processamento de dados
DATA_PROCESSING = "data_processing.py"

###############################################
#analise dos dados
DATA_ANALYSIS = "dataset_analysis.py"

###############################################
#dados de origem
DATALAKE_FILE = "dataset_kaggle.com\Federal_Deposit_Insurance_Corporation_FDIC_Insured_Banks.csv"


###############################################
#definições - staging area
STAGING_AREA = 'dataset_kaggle.com\staging_data.csv'
