#------------------------------------------------------------------------------------------------------------------
#   MLP classifier for the Emojis data set
#------------------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import StratifiedKFold
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

# Input image dimensions
img_rows, img_cols = 32, 32

# Load data
data = np.loadtxt("C:/Users/franu/Downloads/RedesNeuronales/Actividad1/Ejemplo/emojis.txt") 
x = data[:,1:]
y = data[:,0]
print(data)

# Plot one image
ex = x[15,:].reshape(img_rows, img_cols)
plt.imshow(ex, cmap='gray')
plt.show()

#------------------------------------------------------------------------------------------------------------------
# Build MLP classifier
#------------------------------------------------------------------------------------------------------------------
clf = MLPClassifier(hidden_layer_sizes=10*[100], max_iter=10000)
clf.fit(x, y)

#------------------------------------------------------------------------------------------------------------------
# Evaluate MLP classifier
#------------------------------------------------------------------------------------------------------------------
n_splits = 5
kf = StratifiedKFold(n_splits=n_splits, shuffle = True)

cv_y_test = []
cv_y_pred = []

for train_index, test_index in kf.split(x, y):
    
    # Training phase
    x_train = x[train_index, :]
    y_train = y[train_index]    

    clf_cv = MLPClassifier(hidden_layer_sizes=10*[100], max_iter=10000)
    clf_cv.fit(x_train, y_train)

    # Test phase
    x_test = x[test_index, :]
    y_test = y[test_index]

    y_pred = clf_cv.predict(x_test)
    
    cv_y_test.append(y_test)
    cv_y_pred.append(y_pred)

print(classification_report(np.concatenate(cv_y_test), np.concatenate(cv_y_pred)))

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------