import pandas as pd
import numpy as np
from typing_extensions import Union
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder
import sys
# sys.path.append("C:\\Users\\admin\\OneDrive\\Desktop\\ML Ops Workspace\\3-Packaging ML model\\3-3Folder_hierarchy_for_ML\\prediction_model")
    
class MeanImputer(BaseEstimator, TransformerMixin):
    def __init__(self, cols:list) -> None:
        """Args: cols (columns for mean imputation)
            Return: None"""
        self.cols = cols

    def fit(self, X:pd.DataFrame, y:Union[pd.DataFrame, pd.Series]=None):
        """Args: X (df), y (target column/s)
            Return: self (Nothing)"""
        self.mean_dict = {}
        for col in self.cols:
            self.mean_dict[col] = X[col].mean()
        return self
    
    def transform(self, X:pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        for col in self.cols:
            X[col].fillna(self.mean_dict[col], inplace=True)
        return X
    
class ModeImputer(BaseEstimator, TransformerMixin):
    def __init__(self, cols:list) -> None:
        """Args: cols (columns for mode imputation)
            Return: None"""
        self.cols = cols

    def fit(self, X:pd.DataFrame, y:Union[pd.DataFrame, pd.Series]=None):
        """Args: X (df), y (target column/s)
            Return: self (Nothing)"""
        self.mode_dict = {}
        for col in self.cols:
            self.mode_dict[col] = X[col].mode()[0]
        return self
    
    def transform(self, X:pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        for col in self.cols:
            X[col].fillna(self.mode_dict[col], inplace=True)
        return X
    
class LabelEncode(BaseEstimator, TransformerMixin):
    def __init__(self, cols:list) -> None:
        """Args: cols (list)
            Return: None"""
        self.cols = cols
        
    def fit(self, X:pd.DataFrame, y=None):
        """Args: X (Pandas DataFrame)
            Return: self"""
        self.encoder = LabelEncoder()
        return self

    def transform(self, X:pd.DataFrame) -> pd.DataFrame:
        """Args: Nothing to show
            Return: X (Label Encoded pandas dataframe)"""
        X = X.copy()
        for col in self.cols:
            X[col] = self.encoder.fit_transform(X[col])
        return X

class LogTransform(BaseEstimator, TransformerMixin):
    def __init__(self, cols:list) -> None:
        self.cols = cols

    def fit(self, X, y=None):
        """Args: X (df), y (target column/s)
            Returns: self
            
            func: Replacing Zeros with 0.0001
            """
        self.X = X.copy()
        for col in self.cols:
            self.X[col] = X[col].apply(lambda x: 0.0001 if x == 0 else x)
        return self
    
    def transform(self, X:pd.DataFrame) -> pd.DataFrame:
        """Args: Nothing to show
            Return: pd.DataFrame
            func: Log transfomrmation of self.X"""
        for col in self.cols:
            self.X[col] = np.log(self.X[col])
        return self.X

class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, cols:list) -> None:
        """Args: cols (list)
            Return: None"""
        self.cols = cols
        
    def fit(self, X, y=None):
        """Args: X (Pandas DataFrame)
            Return: self"""
        return self

    def transform(self, X:pd.DataFrame) -> pd.DataFrame:
        """Args: Nothing to show
            Return: X (with dropped columns)"""
        X = X.copy()
        X.drop(self.cols, axis='columns', inplace=True)
        return X


