import pathlib
import os
import prediction_model

# REQUIRED PATHS
ROOT_PATH = pathlib.Path(prediction_model.__file__).resolve().parent
DATASETS_PATH = os.path.join(ROOT_PATH, 'datasets')
TRAINED_MODELS_PATH = os.path.join(ROOT_PATH, 'trained_models')

# FOLDER NAMES
TRAIN_DATA = 'train.csv'
TEST_DATA = 'test.csv'

# MODEL
MODEL = 'classifier.pkl'

# COLUMNS CONFIGURATION
FEATURES = ['ApplicantIncome', 
            'CoapplicantIncome', 
            'LoanAmount',
            'Loan_Amount_Term', 
            'Gender', 
            'Married', 
            'Dependents', 
            'Education',
            'Self_Employed', 
            'Credit_History', 
            'Property_Area']

TARGET = 'Loan_Status'

IN_FEATURES = ['ApplicantIncome', 
                'CoapplicantIncome', 
                'LoanAmount',
                'Loan_Amount_Term', 
                'Gender', 
                'Married', 
                'Dependents', 
                'Education',
                'Self_Employed', 
                'Credit_History', 
                'Property_Area']

NUM_FEATURES = ['ApplicantIncome', 
                'CoapplicantIncome', 
                'LoanAmount', 
                'Loan_Amount_Term']

CAT_FEATURES = ['Gender', 
                'Married', 
                'Dependents', 
                'Education', 
                'Self_Employed', 
                'Credit_History', 
                'Property_Area']

ENCODE_FEATURES = CAT_FEATURES

DROPE_FEATURES = ['CoapplicantIncome']
LOG_TRANSFORM_COLS = ['ApplicantIncome', 
                    'CoapplicantIncome']

# DATA PROCESSES
SCALER_USED = 'MinMaxScalar'
ENCODER_USED = 'LabelEncoder'