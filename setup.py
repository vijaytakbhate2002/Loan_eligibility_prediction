import sys
from prediction_model.processing import preprocessing
from prediction_model.config import config

print(len(sys.path))
for path in sys.path:
    print(path.split('\\')[-1])
