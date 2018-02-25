# Data Preprocessing

import numpy as np
import pandas as pd
from processCategoricData import processCategoricData
from processNumericData import processNumericData
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from plot_learning_curve import plot_learning_curve
import math

# Importing da dataset
dataset = pd.read_csv('data/flats.csv')
dataset, y = processNumericData(dataset)
dataset, X = processCategoricData(dataset)

# feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# splitting into train and test set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size = 0.1)

# feature scaling
#sc_X = StandardScaler()
#X_train = sc_X.fit_transform(X_train)
#X_test = sc_X.transform(X_test)

# fitting regression
regressor = LinearRegression()
regressor.fit(X = X_train, y = y_train)
coef = regressor.coef_

# plotting learning curves
plot = plot_learning_curve(regressor, 'Learning Curves', X_scaled, y, ylim=None, cv=None,
                        n_jobs=1, train_sizes=np.linspace(.1, 1.0, 10))
plot.show()

# predict the test set result
y_pred = regressor.predict(X_test)

# calculating cost on test set
J_test = 0
i = 0
for hx in np.nditer(y_pred):
    yt = y_test[i]
    J_test = math.pow(hx - yt, 2) + J_test
    i = i + 1
    
J_test = J_test / (2 * y_test.size)
