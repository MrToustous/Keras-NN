import numpy as np
import pandas as pd

import tensorflow as tf

import data_loader as loader

from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

# sess = tf.Session()
# K.set_session(sess)


# fix random seed for reproducibility
# numpy.random.seed(7)




