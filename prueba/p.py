import pandas as pd
from sklearn.preprocessing import LabelEncoder
# Importar bibliotecas necesarias
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix, classification_report
import datetime
import matplotlib.pyplot as plt
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


df_training_large_even2 = pd.read_csv('training_large_even.csv', low_memory=False)

filtered_df1 = df_training_large_even2[df_training_large_even2['label'] == 1].head(433375)
filtered_df2 = df_training_large_even2[df_training_large_even2['label'] == 0]
unified_df = pd.concat([filtered_df1, filtered_df2], ignore_index=True)

# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Iterate through each column
for column in unified_df.columns:
    if unified_df[column].dtype == 'object':  # Check if the column contains string values
        # Encode only string columns
        unified_df[column] = label_encoder.fit_transform(unified_df[column].astype(str))



# using now() to get current time
current_time = datetime.datetime.now()

# Cargar el conjunto de datos desde el archivo CSV
df = unified_df

# 'X' contiene las características y 'y' contiene las etiquetas
X = df.drop(['label','type'], axis=1) # Excluir la columna de la etiqueta "Class"
y = df['label']  # La columna de etiqueta se llama 'Class'

# Convertir y a one-hot encoding (necesario para la salida de la red neuronal)
y = pd.get_dummies(y)

# Dividir el conjunto de datos en entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.25, random_state=42)

# Convertir los DataFrames de Pandas a arrays NumPy
X_train = np.array(X_train)
X_val = np.array(X_val)
y_train = np.array(y_train)
y_val = np.array(y_val)

# Definir la arquitectura de la red neuronal
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(y_train.shape[1], activation='softmax')  # Capa de salida con activación softmax para clasificación
])

# Compilar el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(X_train, y_train, epochs=8, batch_size=32, validation_data=(X_val, y_val), verbose=1)

# Evaluar el rendimiento del modelo
y_pred_prob = model.predict(X_val)
y_pred = np.argmax(y_pred_prob, axis=1)
accuracy = accuracy_score(np.argmax(y_val, axis=1), y_pred)
f1 = f1_score(np.argmax(y_val, axis=1), y_pred, average='weighted')

# Calcular precisión, recall y matriz de confusión
precision = precision_score(np.argmax(y_val, axis=1), y_pred)
recall = recall_score(np.argmax(y_val, axis=1), y_pred)
conf_matrix = confusion_matrix(np.argmax(y_val, axis=1), y_pred)

# Imprimir las métricas
print("Precision:", precision)
print("Recall:", recall)
print("Matriz de Confusión:")
print(conf_matrix)

# Mostrar métricas de rendimiento
print(f'Accuracy: {accuracy:.4f}')
print(f'F1 Score: {f1:.4f}')
print(" ")

# Generar el classification report
report = classification_report(np.argmax(y_val, axis=1), y_pred)

# Mostrar el classification report
print("Classification Report:")
print(report)
print(f'Tiempo Total : ',datetime.datetime.now()-current_time)

# Extraer la curva de pérdida
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) + 1)

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

model.save('rnn_final.h5')