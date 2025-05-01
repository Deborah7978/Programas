import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generar datos de ejemplo
datos, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Lista para almacenar la suma de errores cuadráticos
suma_errores = []

# Probar diferentes valores de k
valores_k = range(1, 11)
for k in valores_k:
 kmeans = KMeans(n_clusters=k)
 kmeans.fit(datos)
 suma_errores.append(kmeans.inertia_)  

# Graficar el método del codo
plt.figure(figsize=(10, 6))
plt.plot(valores_k, suma_errores, marker='o')
plt.title('Método del Codo para Estimación del Número de Clústeres')
plt.xlabel('Número de Clústeres (k)')
plt.ylabel('Suma de Errores Cuadráticos (suma_errores)')
plt.xticks(valores_k)
plt.grid()
plt.show()