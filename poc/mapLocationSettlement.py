# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:07:14 2018

@author: Attila
"""

import pandas as pd

dataset = pd.read_csv('flat_raw.csv', ';')
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