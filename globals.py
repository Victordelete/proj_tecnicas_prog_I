"""
    Script de configuração geral

    Source do Database: https://www.kaggle.com/datasets/thedevastator/u-s-fdic-insured-banks-and-financial-institution
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
DATA_ANALYSIS = "data_analysis.py"
DATA_APRESENTATION = "data_analysis.ipynb"

###############################################
#dados de origem
DATALAKE_FILE = "dataset_kaggle.com\Federal_Deposit_Insurance_Corporation_FDIC_Insured_Banks.csv"

###############################################
#Define dados
estados_oficiais = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 
                        'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 
                        'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 
                        'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 
                        'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 
                        'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 
                        'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']