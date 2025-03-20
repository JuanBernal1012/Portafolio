# -*- coding: utf-8 -*-
from sklearnex import get_patch_names, patch_sklearn
patch_sklearn()
import numpy as np
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


# Load the Fashion-MNIST dataset 
fashion_mnist = datasets.fetch_openml(name="Fashion-MNIST")
X = np.array(fashion_mnist.data.astype("float32"))
y = np.array(fashion_mnist.target.astype("int"))

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize the data (scale grayscale values from 0 to 255 to the range [0, 1])
X_train /= 255.0
X_test /= 255.0

# Standardize the data (optional but can improve the performance of linear SVM)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and fit the linear SVM model
svm_model_linear = SVC(kernel="linear", C=1.0, random_state=42)
svm_model_linear.fit(X_train, y_train)

# Make predictions on the test set
y_pred_linear = svm_model_linear.predict(X_test)

# Evaluate the linear SVM model's performance
classification_report_linear = classification_report(y_test, y_pred_linear)

# Display the results for linear SVM
print("Linear SVM Classification Report:")
print(classification_report_linear)

# Ajustar el modelo SVM de base radial
svm_model_rbf = SVC(kernel='rbf', C=1.0, gamma='scale')
svm_model_rbf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred_rbf = svm_model_rbf.predict(X_test)

# Evaluar el rendimiento del modelo SVM de base radial
report_rbf = classification_report(y_test, y_pred_rbf)

# Mostrar resultados para SVM de base radial
print("SVM RBF Classification Report:\n", report_rbf)

from sklearn.neural_network import MLPClassifier

# Crear y ajustar el modelo MLP
mlp_model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
mlp_model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred_mlp = mlp_model.predict(X_test)

# Evaluar el rendimiento del modelo MLP
report_mlp = classification_report(y_test, y_pred_mlp)

# Mostrar resultados para MLP
print("MLP Classification Report:\n", report_mlp)

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from minisom import MiniSom
from tensorflow.keras.datasets import fashion_mnist
import numpy as np
import os


# Cargar el conjunto de datos Fashion MNIST
(train_images, train_labels), (_, _) = fashion_mnist.load_data()

# Normalizar las imágenes para escalar los valores de píxeles en el rango [0, 1]
train_images = train_images / 255.0

# Aplanar las imágenes para que puedan ser utilizadas como vectores de entrada para el SOM
train_images_flat = train_images.reshape(train_images.shape[0], -1)

# Definir las dimensiones del SOM (ajústalas según tus necesidades)
som_width = 10
som_height = 10
input_len = train_images_flat.shape[1]

# Inicializar el SOM
som = MiniSom(som_width, som_height, input_len, sigma=1.0, learning_rate=0.5)

# Inicializar los pesos del SOM con valores aleatorios
som.random_weights_init(train_images_flat)

# Entrenar el SOM con los datos
num_epochs = 100
som.train_random(train_images_flat, num_epochs)

# Obtener las etiquetas asignadas a cada neurona en el SOM
labels_map = som.labels_map(train_images_flat, train_labels)

# Visualizar los resultados
fig = plt.figure(figsize=(9, 9))
the_grid = gridspec.GridSpec(som_width, som_height, fig)
for position, label_fracs in labels_map.items():
    plt.subplot(the_grid[som_width-1-position[1], position[0]], aspect=1)
    patches, texts = plt.pie(label_fracs.values())

output_directory = 'resulting_images'
os.makedirs(output_directory, exist_ok=True)  # Crear directorio si no existe
output_path = os.path.join(output_directory, 'som_seed_pies.png')

plt.legend(patches, label_fracs.keys(), bbox_to_anchor=(3.5, 6.5), ncol=3)
plt.savefig(output_path)
plt.show()  