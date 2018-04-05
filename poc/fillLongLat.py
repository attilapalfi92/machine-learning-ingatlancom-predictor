# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:12:31 2018

@author: Attila
"""
import pandas as pd

input = {
            "formatted_address" : None,
            "latitude": None,
            "longitude": None,
            "accuracy": None,
            "google_place_id": None,
            "type": None,
            "postcode": None,
            "input_string": None
        }

data = pd.read_csv('data/flat_raw.csv', ';')
geo = pd.read_csv('data/geocode_results_sum.csv')

data['location'] = data[['settlement', 'settlement_sub']] \
    .apply(lambda s: ' '.join(s), axis=1)

#geo_row = geo.loc[geo['input_string'] == '13. kerület Szegedi út,Hungary']
#geo_row['latitude'].values[0]

longs = []
lats = []
loc_acc = []
for index, row in data.iterrows():
    geo_row = geo.loc[geo['input_string'] == row['location']+',Hungary']
    lats.append(geo_row['latitude'].values[0])
    longs.append(geo_row['longitude'].values[0])
    loc_acc.append(geo_row['accuracy'].values[0])
    
data['longitude'] = longs
data['latitude'] = lats
data['location_accuracy'] = loc_acc

data = data.drop('location', 1).drop('settlement', 1).drop('settlement_sub', 1)

data.to_csv('data/flats2.csv', index=False)
