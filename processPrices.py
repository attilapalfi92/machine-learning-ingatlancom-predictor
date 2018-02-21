# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 11:41:33 2018

@author: attila.palfi
"""

def processPrices (dataset):
    prices = dataset[['price']]
    processed_prices = []
    for p in prices.values:
        [price, _] = p[0].split(' millió Ft')
        processed_prices.append(float(price.replace(',','.')))
    return processed_prices;
