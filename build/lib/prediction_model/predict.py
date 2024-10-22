import sys
sys.path.append('\\'.join(__file__.split('\\')[:-1]))
from processing import data_handling as dh 
from config import config
import numpy as np
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

classification_pipeline = dh.load_pipeline(config.MODEL)

def predict() -> np.ndarray:
    """Args: None
        Return: np.ndarray
        
        func: takes user data, process it, do prediction"""
    user_data = pd.read_csv(os.path.join(config.DATASETS_PATH, config.TEST_DATA))
    user_data = user_data[config.FEATURES]
    pred = classification_pipeline.predict(X=user_data)
    output = np.where(pred == 0,'N','Y')
    return output

# def predict(user_data) -> None:
#     """Args: None
#         Return: None
        
#         func: takes user data, process it, do prediction"""
#     pred = classification_pipeline.predict(X=user_data)
#     output = np.where(pred == 0, 'N','Y')
#     return output
if __name__ == "__main__":
    res = predict()

