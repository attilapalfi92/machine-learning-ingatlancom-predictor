# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:59:08 2018

@author: attila.palfi
"""

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def processCategoricData(dataset):
    
    dataset = dataset.drop('ac', 1).drop('attic', 1).drop('barrier_free', 1)\
    .drop('build_year', 1).drop('energy_cert', 1).drop('garden_connected', 1)
#    dataset['ac'] = dataset['ac'].astype('category')
#    dataset['attic'] = dataset['attic'].astype('category')
#    dataset['barrier_free'] = dataset['barrier_free'].astype('category')
#    dataset['build_year'] = dataset['build_year'].astype('category')
#    dataset['energy_cert'] = dataset['energy_cert'].astype('category')
#    dataset['garden_connected'] = dataset['garden_connected'].astype('category')
#    
    dataset['building_material'] = dataset['building_material'].astype('category')
    dataset['comfort'] = dataset['comfort'].astype('category')
    dataset['cond'] = dataset['cond'].astype('category')
    dataset['heating'] = dataset['heating'].astype('category')
    dataset['parking'] = dataset['parking'].astype('category')
    dataset['sub_type'] = dataset['sub_type'].astype('category')
    dataset['toilet'] = dataset['toilet'].astype('category')

    X = dataset.values
    # encoding categorical data
    categorical_idxs = []
    for column in dataset.columns:
        if dataset[column].dtype.name == 'category':
            idx = dataset.columns.get_loc(column)
            print(idx)
            categorical_idxs.append(idx)
            labelencoder = LabelEncoder()
            X[:, idx] = labelencoder.fit_transform(X[:, idx])
    
    # libs take care of dummy variable trap so I don't have to
    onehotencoder = OneHotEncoder(categorical_features = categorical_idxs)
    X = onehotencoder.fit_transform(X).toarray()

    return dataset, X