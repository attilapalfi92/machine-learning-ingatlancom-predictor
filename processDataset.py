# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:37:19 2018

@author: attila.palfi
"""
from sklearn.preprocessing import Imputer

def processDataset (dataset):
#    dataset = dataset.drop('id', 1)
    
    dataset['price'] = dataset['price'] \
    .apply(lambda p: p.replace(' millió Ft', '').replace(',','.')) \
    .astype(float)
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
    
    dataset['location'] = dataset[['settlement', 'settlement_sub']] \
    .apply(lambda s: ' '.join(s), axis=1)
    
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
    
    # some clearing
    dataset = dataset[dataset['size'] > 12]
    dataset = dataset[dataset['size'] <= 300]
    dataset = dataset[dataset['rooms'] < 12]
    dataset = dataset[dataset['half_rooms'] < 12]
#    
#    building_levels = dataset[['building_levels']].values
#    
#    floor_imputer = Imputer(missing_values="NaN", strategy='most_frequent')    
#    floor_imputer.fit(X[:, dataset.columns.get_loc('floor')])
#                                 
    # TODO: size, settlement
    
    return dataset