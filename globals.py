"""
    Script de configuração geral
"""

import os
import numpy as np
import pandas as pd
import numpy as np
from datetime import datetime as dt

###############################################
#definições gerais
ROOT_PATH = os.path.dirname((os.path.realpath(__file__)))


###############################################
#definições - sistema de ingestão 
DATA_INGESTION = "data_ingestion.py"
DATA_INGESTION_FILE = "dataset_kaggle.com\data_ingestion_file.csv"


###############################################
#processamento de dados
DATA_PROCESSING = "data_processing.py"


###############################################
#dados de origem
DATALAKE_FILE = "dataset_kaggle.com\Federal_Deposit_Insurance_Corporation_FDIC_Insured_Banks.csv"


###############################################
#definições - staging area
STAGING_AREA = 'dataset_kaggle.com\staging_data.csv'
