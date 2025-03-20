#----------------------------------------------------------------------------------------------
#   Neural network for the misterious data 1 set
#------------------------------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd

from sklearn import datasets
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier

from keras.models import Sequential
from keras.layers import Dense
from tensorflow.python.keras.utils import np_utils

# Load data
data = np.loadtxt("C:/Users/franu/Downloads/RedesNeuronales/Actividad1/misterious_data_1.txt") 
x = data[:,1:]
y = data[:,0]

# Train MLP classifier with all the available observations
clf = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=10000)  # hidden_layer_sizes controls the number of neurons of each hidden layer.
clf.fit(x, y)

# 5-fold cross-validation
n_splits=5
kf = StratifiedKFold(n_splits=n_splits, shuffle = True)

cv_y_test = []
cv_y_pred = []

for train_index, test_index in kf.split(x, y):

    # Training phase
    x_train = x[train_index, :]
    y_train = y[train_index]

    clf_i = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=10000)
    clf_i.fit(x_train, y_train)

    # Test phase
    x_test = x[test_index, :]
    y_test = y[test_index]    
    y_pred = clf_i.predict(x_test)

    cv_y_test.append(y_test)
    cv_y_pred.append(y_pred)

print(classification_report(np.concatenate(cv_y_test), np.concatenate(cv_y_pred)))

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------