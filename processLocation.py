# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 11:32:21 2018

@author: attila.palfi
"""

import pandas as pd

def processLocation (dataset):
    dataset['location'] = dataset[['settlement', 'settlement_sub']] \
    .apply(lambda s: ' '.join(s), axis=1)
    
    a_list = list(dataset['location'].unique())
    s_list = list(dataset['settlement'].unique())
    
    as_dict = {}
    for a in a_list:
        for s in s_list:
            if(a.startswith(s)):
                as_dict[a] = s
                break
    
    locs = pd.DataFrame(list(as_dict.items()), columns=['Address', 'Settlement'])
    locs.to_csv('locations.csv', index=False)
    
    return dataset
