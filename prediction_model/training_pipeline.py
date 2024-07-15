import sys
sys.path.append('\\'.join(__file__.split('\\')[:-1]))
from pipeline import classification_pipeline as pipe
from processing import data_handling as dh
from config import config
import numpy as np
import pandas as pd
import os

def train_pipe() -> None:
    """Args: None
        Return: None
        
        func: takes train data, calls fit method of pipeline, dump pipeline"""
    train_data = pd.read_csv(os.path.join(config.DATASETS_PATH, config.TRAIN_DATA))
    train_y = train_data[config.TARGET].map({'N':0, 'Y':1})
    pipe.fit(train_data[config.FEATURES], train_y)
    dh.dump_pipeline(pipe)
