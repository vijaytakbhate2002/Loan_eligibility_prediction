import os 
from prediction_model.config import config
with open(os.path.join(config.ROOT_PATH, 'VERSION')) as f:
    __version__ = f.read().strip()