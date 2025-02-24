import sys
sys.path.append('\\'.join(__file__.split('\\')[:-2]))
from config import config
import pandas as pd
import os
import joblib
from sklearn.base import ClassifierMixin

def load_dataset(file_name:str) -> pd.DataFrame:
    """Args : file_name (str)
        Return : pd.DataFrame """
    path = os.path.join(config.DATASETS_PATH, file_name)
    df = pd.read_csv(path)
    return df

# Serialization
def dump_pipeline(pipeline_to_save) -> None:
    """Args : pipeline_to_save
        Return : None"""
    joblib.dump(pipeline_to_save, os.path.join(config.TRAINED_MODELS_PATH, config.MODEL))
    print("Pipeline dumped successfully")

# Deserialization
def load_pipeline(pipeline_to_load) -> ClassifierMixin:
    """Args : pipeline_to_load
        Return : ClassifierMixin (Model)"""
    classifier = joblib.load(os.path.join(config.TRAINED_MODELS_PATH, config.MODEL))
    print("Pipeline loaded successfully")
    return classifier