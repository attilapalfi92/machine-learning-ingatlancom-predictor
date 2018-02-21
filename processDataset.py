# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:37:19 2018

@author: attila.palfi
"""
from sklearn.preprocessing import Imputer

def processDataset (dataset):
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
    
    floors = dataset[['floor']].values
    for i in range(floors.start, floors.stop):
        if (floors[i][0] == 'földszint'):
            floors[i][0] = '0'
        elif (floors[i][0] == 'félemelet'):
            floors[i][0] = '0.5'
        else:
            floors[i][0] = 'NaN'

    dataset['floor'] = dataset['floor'].astype('float')
    floor_imputer = Imputer(missing_values="NaN", strategy='')
    
    building_levels = dataset[['building_levels']].values
                                     
    # TODO: rooms, size, settlement, building_levels, floor
    
    return dataset