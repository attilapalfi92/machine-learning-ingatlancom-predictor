# Data Preprocessing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from processCategoricData import processCategoricData
from processNumericData import processNumericData
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import math

# Importing da dataset
dataset = pd.read_csv('data/flats.csv')
dataset, y = processNumericData(dataset)
dataset, X = processCategoricData(dataset)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1)

# feature scaling
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# fitting regression
regressor = LinearRegression()
regressor.fit(X = X_train, y = y_train)

# predict the test set result
y_pred = regressor.predict(X_test)

error_sum = 0
i = 0
for hx in np.nditer(y_pred):
    yt = y_test[i]
    error_sum = math.pow(hx - yt, 2) + error_sum
    i = i + 1
    
error_sum = error_sum / (2 * y_test.size)

PolynomialFeatures()