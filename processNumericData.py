# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:57:45 2018

@author: attila.palfi
"""

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
    
    return dataset