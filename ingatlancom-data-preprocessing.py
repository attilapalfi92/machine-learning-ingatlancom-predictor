# Data Preprocessing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from processPrices import processPrices
from processDataset import processDataset

# Importing da dataset

dataset = pd.read_csv('flat_raw.csv', ';')
dataset = processDataset(dataset)
X = dataset.iloc[:,:].drop('price', 1).drop('id', 1).values
y = processPrices(dataset[['price']])