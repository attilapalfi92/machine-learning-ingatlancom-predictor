# Data Preprocessing

import numpy as np
import pandas as pd
from processCategoricData import processCategoricData
from processNumericData import processNumericData
from polynomizer import Polynomizer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from plot_learning_curve import plot_learning_curve
from plot_regularizations import plot_regularizations
from sklearn.metrics import mean_squared_error


class HousingPricePredictor:
    def __init__(self, datasource='data/flats.csv',
                 estimator=Ridge(alpha=0.01)):
        self.datasource = datasource
        self.estimator = estimator

        # Importing da dataset
        initial_dataset = pd.read_csv(datasource)
        poly_degree = 4
        dataset, y, self.imputers, self.polynomizer = processNumericData(initial_dataset, poly_degree)
        dataset, X = processCategoricData(dataset)



# feature scaling
X_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
X_test = X_scaler.transform(X_test)

# fitting regression
# regressor = LinearRegression()
regressor = Ridge(alpha=0.01)  # regularized linear regression
regressor.fit(X=X_train, y=y_train)

# predict the test set result
y_pred = regressor.predict(X_test)

# evaluating
train_score = regressor.score(X_train, y_train)
print('train_score=%s' % train_score)
test_score = regressor.score(X_test, y_test)
print('test_score=%s' % test_score)
scores = cross_val_score(regressor, X=X_train, y=y_train, scoring="neg_mean_squared_error")
print('scores=%s' % scores)
J_test = mean_squared_error(y_test, y_pred)
print('J_test=%s' % J_test)

# ------------ PLOTTING ------------
# plotting learning curves
# rescaling
rescaler = StandardScaler()
X_rescaled = rescaler.fit_transform(X)
plot_learning_curve(regressor, 'Learning Curves', X_rescaled, y, ylim=None, cv=None,
                    n_jobs=1, train_sizes=np.linspace(.1, 1.0, 10))

# plotting by regularization parameters
alphas = np.logspace(-5, 1, 60)
plot_regularizations(X_train, X_test, y_train, y_test, alphas)