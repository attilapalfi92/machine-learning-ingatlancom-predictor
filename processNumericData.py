# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:57:45 2018

@author: attila.palfi
"""
from sklearn.preprocessing import Imputer
import numpy as np

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
    dataset = dataset[dataset['size'] > 12]
    dataset = dataset[dataset['size'] <= 300]
    dataset = dataset[dataset['rooms'] < 12]
    dataset = dataset[dataset['half_rooms'] < 12]
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
    
    return dataset, X, y