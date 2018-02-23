# Data Preprocessing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from processPrices import processPrices
from processDataset import processDataset

# Importing da dataset

dataset = pd.read_csv('flat_raw.csv', ';')
X, y = processDataset(dataset)