import numpy as np
from sklearn.neighbors import KNeighborsClassifier

#Conjunto de Datos
data = {
    'Caso' : [1, 2, 3, 4, 5, 6, 7, 8],
    'X1' : [2, 4, 1, 2, 2, 2, 3, 3],
    'X2' : [0, 4, 1, 4, 2, 3, 4, 3],
    'Clase' : [0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Creación del clasificador k-NN
k = 1
knn = KNeighborsClassifier(n_neighbors=k, metric='manhattan')

# Caso a clasificar
nuevo_caso = np.array([[2.5, 2.5]])

# Predicción
prediccion = knn.predict(nuevo_caso)

# Mostrar resultado
print(f"La clase predicha para el caso {nuevo_caso[0]} es: {prediccion[0]}")