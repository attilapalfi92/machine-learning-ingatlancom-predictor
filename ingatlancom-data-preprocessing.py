# Data Preprocessing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from processCategoricData import processCategoricData
from processNumericData import processNumericData
import math
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Importing da dataset
dataset = pd.read_csv('data/flats.csv')
dataset, X, y = processNumericData(dataset)
dataset, X = processCategoricData(dataset, X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# feature scaling
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
