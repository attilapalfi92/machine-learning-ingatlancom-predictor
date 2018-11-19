# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:07:14 2018

@author: Attila
"""

import pandas as pd

dataset = pd.read_csv('data_2018_11/raw_data.csv', ',')
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
locs.to_csv('data_2018_11/locations.csv', index=False)

for i in range(0, locs.shape[0], 2500):
    filename = 'data_2018_11/locations_' + str(i) + '_' + str(i + 2500) + '.csv'
    print(filename)
    locs[i:i+2500].to_csv(filename, index=False)
