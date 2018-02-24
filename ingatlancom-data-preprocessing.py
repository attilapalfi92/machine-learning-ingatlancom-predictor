# Data Preprocessing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from processCategoricData import processCategoricData
from processNumericData import processNumericData
import math

# Importing da dataset
dataset = pd.read_csv('data/flats.csv')
dataset, X, y = processNumericData(dataset)
dataset, X = processCategoricData(dataset, X)

i = 0
j = 0
for row in X:
    j = 0
    for value in row:
        value
        if (math.isnan(value)):
            print('i: ' + str(i))
            print('j: ' + str(j))
        j = j + 1
    i = i + 1