# Data Preprocessing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from processPrices import processPrices
from processDataset import processDataset

# Importing da dataset

dataset = pd.read_csv('data/flat_raw.csv', ';')
dataset = processDataset(dataset)

y = dataset['price'].values
dataset = dataset.drop('id', 1).drop('price', 1)
X = processCategoricData(dataset)

# imputing
#floor_imputer = Imputer(missing_values="NaN", strategy='most_frequent')    
#floor_imputer.fit(X[:, dataset.columns.get_loc('floor')])

# categorical data
X = dataset.values
    categorical_idxs = []
    for column in dataset.columns:
        if dataset[column].dtype.name == 'category':
            idx = dataset.columns.get_loc(column)
            print(idx)
            categorical_idxs.append(idx)
            labelencoder = LabelEncoder()
            X[:, idx] = labelencoder.fit_transform(X[:, idx])
    
    onehotencoder = OneHotEncoder(categorical_features = categorical_idxs)
    X = onehotencoder.fit_transform(X).toarray()