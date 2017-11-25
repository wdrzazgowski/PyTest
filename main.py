import pandas as pd

white = pd.read_csv("c:\git\playground\Keras_tutorial\winequality-white.csv", sep=';')
#print(white.info)

red = pd.read_csv("c:\git\playground\Keras_tutorial\winequality-red.csv", sep=';')
#print(red.info)

#red.head()
#white.tail()
#print(red.sample(5))
#print(white.describe())
#print(pd.isnull(red))

import numpy as np
print(np.histogram(red.alcohol, bins=[7,8,9,10,11,12,13,14,15]))
print(np.histogram(white.alcohol, bins=[7,8,9,10,11,12,13,14,15]))