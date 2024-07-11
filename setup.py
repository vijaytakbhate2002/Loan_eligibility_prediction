import os
import io
from pathlib import Path
from prediction_model.config import config
import sys

NAME = "Loan Eligibility Prediction"
DESCRIPTION = "Machine Learning model for loan eligibility prediction"
URL = 'https://github.com/vijaytakbhate2002/Loan_eligibility_prediction.git'
EMAIL = 'takbhatevijay@gmail.com'
AUTHOR_NAME = 'Vijay Dipak Takbhate'
REQUIRED_PYTHON = '>=3.12.4'

# reading requirements.txt file
def read_req(fname='reqirements.txt', encoding='utf8') -> None:
    with io.open(os.path.join(config.ROOT_PATH, fname)) as f:
        return f.read().splitlines()
    
# 