import tensorflow as tf 
from tensorflow.keras.datasets import mnist 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.callbacks import EarlyStopping 
from tensorflow.keras.utils import to_categorical 
import matplotlib.pyplot as plt


(x_entrenamiento, y_entrenamiento), (x_prueba, y_prueba) = mnist.load_data()

x_entrenamiento = x_entrenamiento / 255.0 
x_prueba = x_prueba / 255.0

y_entrenamiento = to_categorical(y_entrenamiento, 10) 
y_prueba = to_categorical(y_prueba, 10)

#Crear el modelo secuencial con capas adicionales

modelo = Sequential([
    Flatten(input_shape=(28, 28)), 
    Dense(256, activation='relu'), 
    Dropout(0.3), 
    Dense(128, activation='relu'), 
    Dense(10, activation='softmax')
])

modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

detener_temprano = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

historial = modelo.fit( 
    x_entrenamiento, y_entrenamiento,
    epochs=15, 
    batch_size=32, 
    validation_split=0.1, 
    callbacks=[detener_temprano], 
    verbose=2 
)

#Evaluar el modelo en el conjunto de prueba

perdida, precision = modelo.evaluate(x_prueba, y_prueba) 
print(f"\nPérdida en test: {perdida:.4f}") 
print(f"Precisión en test: {precision:.4f}")

#Graficar la precisión y la pérdida
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1) 
plt.plot(historial.history['precisión'], label='Entrenamiento') 
plt.plot(historial.history['val_precisión'], label='Validación') 
plt.title('Precisión por época') 
plt.xlabel('Época') 
plt.ylabel('Precisión') 
plt.legend()

plt.subplot(1, 2, 2) 
plt.plot(historial.history['pérdida'], label='Entrenamiento') 
plt.plot(historial.history['val_pérdida'], label='Validación') 
plt.title('Pérdida por época') 
plt.xlabel('Época') 
plt.ylabel('Pérdida') 
plt.legend()

plt.tight_layout()
plt.show()