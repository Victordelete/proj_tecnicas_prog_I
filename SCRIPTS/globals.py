"""
    Script de configuração geral
"""

import os
from datetime import datetime as datetime
import pandas as pd
import numpy as np
from pathlib import Path

###############################################
#definições gerais
ROOT_PATH = os.path.dirname((os.path.realpath(__file__)))
DATAFRAME_PATH = str(Path(__file__).parents[1]) + r"\dataset"
RAW_TABLE = "dataset_kaggle.com\Federal_Deposit_Insurance_Corporation_FDIC_Insured_Banks.csv"

###############################################
#definições - sistema de ingestão 
