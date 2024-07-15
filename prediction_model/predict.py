import sys
sys.path.append('\\'.join(__file__.split('\\')[:-1]))
from processing import data_handling as dh 
from config import config
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

classification_pipeline = dh.load_pipeline(config.MODEL)

def predict(user_data:np.ndarray) -> str:
    """Args: np.ndarray
        Return: str
        
        func: takes user data, process it, do prediction"""
    if isinstance(user_data, (list, np.ndarray)):
        raise ValueError("Unsupported data type, expected pd.DataFrame")
    if isinstance(user_data, (pd.DataFrame)):
        user_data = user_data[config.FEATURES]

    pred = classification_pipeline.predict(user_data)
    output = 'N' if pred[0] == 0 else 'Y'
    return output
