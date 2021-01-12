#Read in Data

import tensorflow as tf
import numpy as np
from tensorflow import keras
import pandas as pd

Path = "/Users/dhjoo/Desktop/Workspace/stock/archive/individual_stocks_5yr/"
data = pd.read_csv(Path+"AAPL_data")
print(data.shape)
