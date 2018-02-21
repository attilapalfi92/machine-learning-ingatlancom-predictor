# Data Preprocessing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from processPrices import processPrices
from processDataset import processDataset

# Importing da dataset

dataset = pd.read_csv('flat_raw.csv', ';')
dataset = processDataset(dataset)
dataset['location'].to_csv('locations.csv', index=False)