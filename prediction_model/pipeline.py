from config import config
from processing import preprocessing
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression

classification_pipeline = Pipeline([
    ('MeanImputer', preprocessing.MeanImputer(cols=config.NUM_FEATURES)),
    ('ModeImputer', preprocessing.ModeImputer(cols=config.CAT_FEATURES)),
    ('LablEncoder', preprocessing.LabelEncode(cols=config.ENCODE_FEATURES)),
    ('LogTransformation', preprocessing.LogTransform(cols=config.LOG_TRANSFORM_COLS)),
    ('DropColumns', preprocessing.DropColumns(cols=config.DROPE_FEATURES)),
    ('MinMaxScale', MinMaxScaler()),
    ('LogisticRegression', LogisticRegression(random_state=0))
])