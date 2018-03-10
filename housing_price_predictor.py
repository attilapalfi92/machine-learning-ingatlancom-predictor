# Data Preprocessing

import numpy as np
import pandas as pd

from numeric_data_processor import NumericDataProcessor
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from plot_learning_curve import plot_learning_curve
from plot_regularizations import plot_regularizations
from sklearn.metrics import mean_squared_error


class HousingPricePredictor:
    def __init__(self, datasource='data/flats.csv',
                 estimator=Ridge(alpha=0.01)):

        self.estimator = estimator

        # Importing da dataset
        initial_dataset = pd.read_csv(datasource)

        # numeric data
        self.numericDataProcessor = NumericDataProcessor(initial_dataset)
        dataset = self.numericDataProcessor.getDataset()
        y = self.numericDataProcessor.getY()

        # categoric data
        dataset, X = processCategoricData(dataset)

        # feature scaling
        self.standardScaler = StandardScaler()
        X_train = self.standardScaler.fit_transform(X)
        self.estimator.fit(X=X_train, y=y)

    def predict(self, dataset):
        dataset = self.numericDataProcessor.process(dataset)