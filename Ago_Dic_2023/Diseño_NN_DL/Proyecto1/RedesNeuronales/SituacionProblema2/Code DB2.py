# -*- coding: utf-8 -*-
import os
import numpy as np
from skimage import io
from skimage.transform import resize
from skimage.feature import graycomatrix, graycoprops
from skimage.color import rgb2gray, rgb2hsv
from skimage import img_as_ubyte
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearnex import get_patch_names, patch_sklearn
from minisom import MiniSom
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

patch_sklearn()

# Definir la ruta de la carpeta que contiene las carpetas de personas
base_folder = "C://Users//Juani//OneDrive//Escritorio//OMAR SITUACION PROBLEMA NUEVA//Biomas"

# Inicializar listas para almacenar imágenes y etiquetas
X = []
y = []
scale = 8
img_width = int(1920/scale)
img_height = int(1080/scale)

# Recorrer cada carpeta de personas
for person_folder in os.listdir(base_folder):
    if os.path.isdir(os.path.join(base_folder, person_folder)):
        # Recorrer cada imagen en la carpeta
        for filename in os.listdir(os.path.join(base_folder, person_folder)):
            img_path = os.path.join(base_folder, person_folder, filename)
            
            # Cargar la imagen y redimensionarla
            rgb = io.imread(img_path)
            rgb_resized = resize(rgb, (img_height, img_width), anti_aliasing=True)
            
            # Extracción de características (histogramas de color y descriptores de textura)
            nbins = 16
            rh = np.histogram(rgb_resized[:,:,0].flatten(), nbins, density=True)
            gh = np.histogram(rgb_resized[:,:,1].flatten(), nbins, density=True)
            bh = np.histogram(rgb_resized[:,:,2].flatten(), nbins, density=True)
            hist_descriptor = np.concatenate((rh[0], gh[0], bh[0]))
            
            gray_resized = img_as_ubyte(rgb2gray(rgb_resized))
            glcm = graycomatrix(gray_resized, distances=[5], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4])
            texture_desc = [graycoprops(glcm, 'dissimilarity')[0, 0], graycoprops(glcm, 'homogeneity')[0, 0],
                            graycoprops(glcm, 'energy')[0, 0], graycoprops(glcm, 'correlation')[0, 0]]
            
            # Concatenar características en un solo vector
            features = np.concatenate((hist_descriptor, texture_desc))
            
            # Agregar la imagen y la etiqueta a las listas
            X.append(features)
            y.append(person_folder)

# Convertir listas a matrices numpy
X = np.array(X)
y = np.array(y)

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Normalizar los datos
X_train /= 255.0
X_test /= 255.0

# Estandarizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear y ajustar el modelo SVM lineal
svm_model_linear = SVC(kernel="linear", C=1.0, random_state=42)
svm_model_linear.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred_linear = svm_model_linear.predict(X_test)

# Evaluar el rendimiento del modelo SVM lineal
classification_report_linear = classification_report(y_test, y_pred_linear)

# Mostrar resultados para SVM lineal
print("Linear SVM Classification Report:")
print(classification_report_linear)

# Crear y ajustar el modelo SVM de base radial
svm_model_rbf = SVC(kernel='rbf', C=1.0, gamma='scale')
svm_model_rbf.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred_rbf = svm_model_rbf.predict(X_test)

# Evaluar el rendimiento del modelo SVM de base radial
report_rbf = classification_report(y_test, y_pred_rbf)

# Mostrar resultados para SVM de base radial
print("SVM RBF Classification Report:\n", report_rbf)

# Crear y ajustar el modelo MLP
mlp_model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
mlp_model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred_mlp = mlp_model.predict(X_test)

# Evaluar el rendimiento del modelo MLP
report_mlp = classification_report(y_test, y_pred_mlp)

# Mostrar resultados para MLP
print("MLP Classification Report:\n", report_mlp)

# Define a pipeline for linear SVM
svm_linear_pipeline = make_pipeline(StandardScaler(), SVC(kernel="linear", C=1.0, random_state=42))

# Define a pipeline for radial SVM
svm_rbf_pipeline = make_pipeline(StandardScaler(), SVC(kernel='rbf', C=1.0, gamma='scale'))

# Define a pipeline for MLP
mlp_pipeline = make_pipeline(StandardScaler(), MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42))

# Perform cross-validation for linear SVM
linear_scores = cross_val_score(svm_linear_pipeline, X, y, cv=5)  
print("Linear SVM Cross-Validation Scores:", linear_scores)
print("Mean Linear SVM Cross-Validation Score:", np.mean(linear_scores))

# Perform cross-validation for radial SVM
rbf_scores = cross_val_score(svm_rbf_pipeline, X, y, cv=5)  
print("RBF SVM Cross-Validation Scores:", rbf_scores)
print("Mean RBF SVM Cross-Validation Score:", np.mean(rbf_scores))

# Perform cross-validation for MLP
mlp_scores = cross_val_score(mlp_pipeline, X, y, cv=5)
print("MLP Cross-Validation Scores:", mlp_scores)
print("Mean MLP Cross-Validation Score:", np.mean(mlp_scores))

# SOM
som_width = 10
som_height = 10
input_len = X_train.shape[1]

# Inicializar el SOM
som = MiniSom(som_width, som_height, input_len, sigma=1.0, learning_rate=0.5)

# Inicializar los pesos del SOM con valores aleatorios
som.random_weights_init(X_train)

# Entrenar el SOM con los datos de entrenamiento
num_epochs = 100
som.train_random(X_train, num_epochs)

# Obtener las etiquetas asignadas a cada neurona en el SOM
labels_map = som.labels_map(X_train, y_train)

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
