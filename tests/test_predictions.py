import sys
sys.path.append("C:\\Users\\admin\\OneDrive\\Desktop\\ML Ops Workspace\\3-Packaging ML model\\3-3Folder_hierarchy_for_ML")
from prediction_model.config import config
import os
from predict import predict 
import pandas as pd
import numpy as np
import pytest

# will create Fixture method with decorator of pytest.fixture

# create function to first test output of model is None or not None
# create function to first test output of model is str or not
# create function to first test output of model is 'Y'


@pytest.fixture
def test_prediction():
    """ Args: None
        Return: np.ndarray (predicted output) """
    test_data = pd.read_csv(os.path.join(config.DATASETS_PATH, config.TEST_DATA))
    first_row = test_data[:1]
    res = predict(first_row)
    return res

def test_none_out():
    assert test_prediction.get('predictions')[0] is not None

def test_str_out():
    assert isinstance(test_prediction.get('predictions')[0], str)

def test_y_out():
    assert test_prediction.get('predictions')[0] == 'Y'

