# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 18:27:36 2018

@author: Attila
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import pylab as pl
from poc.processDataset import processDataset

dataset = pd.read_csv('flat_raw.csv', ';')
dataset = processDataset(dataset)

# price:
prices = dataset['price'].values
prices.sort()
prices = np.log(prices)

pdf = stats.norm.pdf(prices, np.mean(prices), np.std(prices))
pl.plot(prices, pdf,'-o')
pl.hist(prices, normed = True)
pl.show()

# size:
sizes = dataset['size'].values
sizes = np.array(list(map(lambda x: 1.0 if np.isnan(x) else x, sizes)))
sizes.sort()
sizes = np.log(sizes)

pdf = stats.norm.pdf(sizes, np.mean(sizes), np.std(sizes))
pl.plot(sizes, pdf,'-o')
pl.hist(sizes, normed = True)
pl.show()

# rooms:
rooms = dataset['rooms'].values
rooms = np.array(list(map(lambda x: 1.0 if np.isnan(x) else x, rooms)))
rooms.sort()
rooms = np.log(rooms)

pdf = stats.norm.pdf(rooms, np.mean(rooms), np.std(rooms))
pl.plot(rooms, pdf,'-o')
pl.hist(rooms, normed = True)
pl.show()

# code multivariate gaussian anomaly deteaction later
