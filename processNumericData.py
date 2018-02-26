# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:57:45 2018

@author: attila.palfi
"""
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import pandas as pd

def processNumericData(dataset):
    dataset['floor'] = dataset['floor'] \
    .apply(lambda f: f.replace('nincs megadva', 'NaN')).astype(float)
    
    dataset['building_levels'] = dataset['building_levels'] \
    .apply(lambda f: f.replace('nincs megadva', 'NaN')).astype(float)
    
    room_data = dataset['rooms'].str.split(' \+ ', 1, expand = True)
    dataset['rooms'] = room_data[0].astype(str) \
    .apply(lambda hr: hr.replace(' fél', '')).astype(float)
    
    dataset['half_rooms'] = room_data[1].astype(str) \
    .apply(lambda hr: hr.replace(' fél', '')) \
    .apply(lambda hr: hr.replace('None', '0')).astype(float)
    
    dataset['size'] = dataset['size'].astype(str) \
    .apply(lambda s: s.replace(' m²', '')).apply(lambda s: s.replace(' ','')) \
    .astype(float)
    
    dataset['price'] = dataset['price'] \
    .apply(lambda p: p.replace(' millió Ft', '').replace(',','.')) \
    .astype(float)
    
    # some clearing
    dataset = dataset[dataset['size'] > 20]
    dataset = dataset[dataset['size'] < 250]
    dataset = dataset[dataset['rooms'] < 10]
    dataset = dataset[dataset['half_rooms'] < 10]
    dataset = dataset[np.isfinite(dataset['longitude'])]
    dataset = dataset[np.isfinite(dataset['latitude'])]
    
    y = dataset['price'].values
    dataset = dataset.drop('id', 1).drop('price', 1)
    X = dataset.values
    
    # imputing
    def impute(dataset, X, column_name):
        idx = dataset.columns.get_loc(column_name)
        imputer = Imputer(missing_values="NaN", strategy='mean', axis = 0)
        imputer.fit(X[:, idx:idx + 1])
        X[:, idx:idx+1] = imputer.transform(X[:, idx:idx + 1])
        return X
    
    X = impute(dataset, X, 'floor')
    X = impute(dataset, X, 'building_levels')
    dataset = pd.DataFrame(X, columns = dataset.columns)


    # adding polynomial features
    features_to_poly = dataset[['rooms','half_rooms','size', 'latitude', 'longitude']].values
    poly_feat = PolynomialFeatures(degree = 4)
    X_poly = poly_feat.fit_transform(features_to_poly)
    poly_dataset = pd.DataFrame(X_poly)
    
    dropped_dataset = dataset.drop('rooms', 1).drop('half_rooms', 1).drop('size', 1)\
    .drop('latitude', 1).drop('longitude', 1)
    dataset = pd.concat([dropped_dataset, poly_dataset], axis=1)
    
    return dataset, y













