# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:37:19 2018

@author: attila.palfi
"""
from sklearn.preprocessing import Imputer

def processDataset (dataset):
    dataset = dataset.drop('price', 1).drop('id', 1)
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
    dataset['floor'] = dataset['floor'].apply(lambda f: f.replace('nincs megadva', 'NaN')).astype('float')
    dataset['building_levels'] = dataset['building_levels'].apply(lambda f: f.replace('nincs megadva', 'NaN')).astype('float')
    
    room_data = dataset['rooms'].str.split(' \+ ', 1, expand = True)
    dataset['rooms'] = room_data[0].astype(str)
    dataset['rooms'] = dataset['rooms'].apply(lambda hr: hr.replace(' fél', ''))
    dataset['rooms'] = dataset['rooms'].astype(float)
    dataset['half_rooms'] = room_data[1].astype(str)
    dataset['half_rooms'] = dataset['half_rooms'].apply(lambda hr: hr.replace(' fél', ''))
    dataset['half_rooms'] = dataset['half_rooms'].apply(lambda hr: hr.replace('None', '0'))
    dataset['half_rooms'] = dataset['half_rooms'].astype(float)
    
    
    X = dataset.values
#    
#    building_levels = dataset[['building_levels']].values
#    
#    floor_imputer = Imputer(missing_values="NaN", strategy='most_frequent')    
#    floor_imputer.fit(X[:, dataset.columns.get_loc('floor')])
#                                 
    # TODO: size, settlement
    
    return X