# -*- coding: utf-8 -*-
import os
import numpy as np
from skimage import io
from skimage.transform import resize
from skimage.color import rgb2gray, rgb2hsv
from skimage import img_as_ubyte
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report
from sklearn.utils import shuffle
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

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
            
            # Agregar la imagen y la etiqueta a las listas
            X.append(rgb_resized)
            y.append(person_folder)

# Convertir listas a matrices numpy
X = np.array(X)
y = np.array(y)

# One-hot encode the labels
le = LabelEncoder()
y = le.fit_transform(y)

# Shuffle the data
X, y = shuffle(X, y, random_state=42)

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar los datos
X_train = X_train / 255.0
X_test = X_test / 255.0

# Reshape the data to be compatible with CNN
X_train = X_train.reshape(-1, img_height, img_width, 3)
X_test = X_test.reshape(-1, img_height, img_width, 3)

# Definir el modelo CNN
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(len(np.unique(y)), activation='softmax'))

# Compilar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluar el modelo
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc}")

# Predicciones
predictions = model.predict(X_test)
y_pred = np.argmax(predictions, axis=1)
print(classification_report(y_test, y_pred, target_names=le.classes_))
