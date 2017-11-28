import pandas as pd
import numpy as np

white = pd.read_csv("c:\git\playground\Keras_tutorial\winequality-white.csv", sep=';')
red = pd.read_csv("c:\git\playground\Keras_tutorial\winequality-red.csv", sep=';')

# Add `type` column to `red` with value 1
red['type'] = 1

# Add `type` column to `white` with value 0
white['type'] = 0

# Append `white` to `red`
wines = red.append(white, ignore_index=True)

# Import `train_test_split` from `sklearn.model_selection`
from sklearn.model_selection import train_test_split

# Specify the data 
X=wines.ix[:,0:11]
#print(X)

# Specify the target labels and flatten the array 
y=np.ravel(wines.type)
#print(y)

# Split the data up in train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# Import `StandardScaler` from `sklearn.preprocessing`
from sklearn.preprocessing import StandardScaler

# Define the scaler 
scaler = StandardScaler().fit(X_train)

# Scale the train set
X_train = scaler.transform(X_train)

# Scale the test set
X_test = scaler.transform(X_test)



from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

model.add(Dense(12, activation='relu', input_shape=(11,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', 
	optimizer =  'adam',
	metrics = ['accuracy'])

model.fit(X_train, y_train, epochs = 20, batch_size = 1, verbose = 1)