# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:59:08 2018

@author: attila.palfi
"""

from sklearn.preprocessing import LabelEncoder

def processCategoricData(dataset):
    dataset = dataset.drop('price').drop('id')
    
    dataset['ac'] = dataset['ac'].astype('category')
    dataset['attic'] = dataset['attic'].astype('category')
    dataset['barrier_free'] = dataset['barrier_free'].astype('category')
    dataset['build_year'] = dataset['build_year'].astype('category')
    dataset['building_material'] = dataset['building_material'].astype('category')
    dataset['comfort'] = dataset['comfort'].astype('category')
    dataset['cond'] = dataset['cond'].astype('category')
    dataset['energy_cert'] = dataset['energy_cert'].astype('category')
    dataset['garden_connected'] = dataset['garden_connected'].astype('category')
    dataset['heating'] = dataset['heating'].astype('category')
    dataset['parking'] = dataset['parking'].astype('category')
    dataset['sub_type'] = dataset['sub_type'].astype('category')
    dataset['toilet'] = dataset['toilet'].astype('category')
    
    X = dataset.values
    index = dataset.columns.get_loc('ac')
    labelencoder = LabelEncoder()
    labelencoder.fit_transform(X[:, index])
    
    return X