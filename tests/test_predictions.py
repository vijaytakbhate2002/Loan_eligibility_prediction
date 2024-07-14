import sys
sys.path.append('\\'.join(__file__.split('\\')[:-2]))
from prediction_model.config import config
import os
from prediction_model.predict import predict 
import pandas as pd
import numpy as np
import pytest

# will create Fixture method with decorator of pytest.fixture

# create function to first test output of model is None or not None
# create function to first test output of model is str or not
# create function to first test output of model is 'Y'


@pytest.fixture
def single_prediction():
    """ Args: None
        Return: np.ndarray (predicted output) """
    test_data = pd.read_csv(os.path.join(config.DATASETS_PATH, config.TEST_DATA))
    first_row = test_data[:1]
    res = predict(first_row)
    return res

def test_none_out(single_prediction):
    assert single_prediction is not None

def test_str_out(single_prediction):
    assert type(single_prediction[0]) == np.str_

def test_y_out(single_prediction):
    assert single_prediction[0] == 'Y'

