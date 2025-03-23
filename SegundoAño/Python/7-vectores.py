import numpy as np

class DistanciaVectores:
    def __init__(self):
        pass

    # Distancia Euclidiana
    def distancia_euclidiana(self, vec1, vec2):
        return np.sqrt(np.sum((vec1 - vec2) ** 2))

    # Distancia Euclidiana Normalizada
    def distancia_euclidiana_normalizada(self, vec1, vec2):
        norm1 = vec1 / np.linalg.norm(vec1)
        norm2 = vec2 / np.linalg.norm(vec2)
        return np.sqrt(np.sum((norm1 - norm2) ** 2))

    # Distancia Chebyshev
    def distancia_chebyshev(self, vec1, vec2):
        return np.max(np.abs(vec1 - vec2))

    # Distancia Manhattan
    def distancia_manhattan(self, vec1, vec2):
        return np.sum(np.abs(vec1 - vec2))

    def encontrar_vectores_similares(self, nombre_distancia, nuevo_vector, base_datos):
        # Obtener la función de distancia usando reflection
        funcion_distancia = getattr(self, nombre_distancia, None)
        if funcion_distancia is None:
            raise ValueError(f"La función de distancia '{nombre_distancia}' no está definida.")

        distancias = []
        for vector_db in base_datos:
            # Calcular la distancia entre el nuevo vector y el vector de la base de datos
            dist = funcion_distancia(np.array(nuevo_vector), np.array(vector_db))
            distancias.append((vector_db, dist))
    
        # Ordenar los vectores por distancia (menor primero)
        distancias.sort(key=lambda x: x[1])

        # Retornar solo los vectores ordenados
        return [vector for vector, _ in distancias]