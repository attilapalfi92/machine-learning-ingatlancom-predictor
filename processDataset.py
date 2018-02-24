# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:37:19 2018

@author: attila.palfi
"""
from sklearn.preprocessing import Imputer
from processLocation import processLocation
from processNumericData import processNumericData
from processCategoricData import processCategoricData

def processDataset (dataset):
#    dataset = dataset.drop('id', 1)
    
    dataset = processLocation(dataset)
    dataset = processNumericData(dataset)
    
    # some clearing
    dataset = dataset[dataset['size'] > 12]
    dataset = dataset[dataset['size'] <= 300]
    dataset = dataset[dataset['rooms'] < 12]
    dataset = dataset[dataset['half_rooms'] < 12]
    
    return X, y