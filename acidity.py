import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

white = pd.read_csv("c:\git\playground\Keras_tutorial\winequality-white.csv", sep=';')
red=pd.read_csv("c:\git\playground\Keras_tutorial\winequality-red.csv", sep=';')

np.random.seed(570)

redlabels = np.unique(red['quality'])
whitelabels = np.unique(white['quality'])
