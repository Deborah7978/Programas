# Problema:
# Obtener un valor de π calculando la suma siguiente para n=200:
# 4∑k=1n(−1)k+12k−1

def calcular_pi(n):
    suma = 0  # Inicializamos la suma en 0

    for k in range(1, n + 1):
        # Calculamos cada término de la serie
        termino = (-1)(k + 1) / (2 * k - 1)
        suma += termino  # Sumamos el término a la suma total

    pi_aproximado = 4 * suma  # Multiplicamos la suma por 4 para obtener π
    return pi_aproximado

# Definimos el valor de n
n = 200

# Llamamos a la función y mostramos el resultado
pi_estimado = calcular_pi(n)

print(f"Valor estimado de π con n={n}: {pi_estimado}")