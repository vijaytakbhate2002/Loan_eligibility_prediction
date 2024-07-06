from pipeline import classification_pipeline as pipe
from prediction_model.processing import data_handling as dh 
from prediction_model.config import config
import numpy as np
import pandas as pd
import os

classification_pipeline = dh.load_pipeline(config.MODEL)

def predict() -> None:
    """Args: None
        Return: None
        
        func: takes user data, process it, do prediction"""
    user_data = pd.read_csv(os.path.join(config.DATASETS_PATH, config.TEST_DATA))
    user_data = user_data[config.FEATURES]
    pred = classification_pipeline.predict(X=user_data)
    output = np.where(pred == 0,'N','Y')
    return output

if __name__ == "__main__":
    predict()
