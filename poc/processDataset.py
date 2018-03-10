# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:37:19 2018

@author: attila.palfi
"""
from poc.process_numeric_data import process_numeric_data


def processDataset (dataset):
#    dataset = dataset.drop('id', 1)
    
    dataset = process_numeric_data(dataset)
    
    # some clearing
    dataset = dataset[dataset['size'] > 12]
    dataset = dataset[dataset['size'] <= 300]
    dataset = dataset[dataset['rooms'] < 12]
    dataset = dataset[dataset['half_rooms'] < 12]
    
    return dataset