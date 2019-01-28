# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 13:12:31 2018

@author: Attila
"""
import pandas as pd

geo1 = pd.read_csv('data_2018_11/geocode_results_0_2500.csv')
geo2 = pd.read_csv('data_2018_11/geocode_results_2500_5000.csv')
geo3 = pd.read_csv('data_2018_11/geocode_results_5000_7500.csv')
geo4 = pd.read_csv('data_2018_11/geocode_results_7500_10000.csv')
geo5 = pd.read_csv('data_2018_11/geocode_results_10000_12500.csv')

geos = [geo1, geo2, geo3, geo4, geo5]

geo_sum = pd.concat(geos)
geo_sum.to_csv('data_2018_11/geocode_results_sum.csv')


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

data = pd.read_csv('data_2018_11/raw_data.csv', ',')
geo_sum = pd.read_csv('data_2018_11/geocode_results_sum.csv')

data['location'] = data[['settlement', 'settlement_sub']] \
    .apply(lambda s: ' '.join(s), axis=1)

#geo_row = geo.loc[geo['input_string'] == '13. kerület Szegedi út,Hungary']
#geo_row['latitude'].values[0]

longs = []
lats = []
loc_acc = []
for index, row in data.iterrows():
    geo_row = geo_sum.loc[geo_sum['input_string'] == row['location']+',Hungary']
    lats.append(geo_row['latitude'].values[0])
    longs.append(geo_row['longitude'].values[0])
    loc_acc.append(geo_row['accuracy'].values[0])
    
data['longitude'] = longs
data['latitude'] = lats
data['location_accuracy'] = loc_acc


data.to_csv('data_2018_11/flats.csv', index=False)
