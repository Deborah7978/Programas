# Problema:
# Genera una lista que contenga el cuadrado de los números pares y el cubo de los impares 
# entre 1 y 100 (inclusive). Calcula cuantos números de esa lista debes sumar para que el 
# resultado de la suma sea lo más cercano posible, pero inferior, a un millón.

numeros = []
for i in range(1, 101):
    if i % 2 == 0:
        numeros.append(i ** 2)  # Cuadrado de pares
    else:
        numeros.append(i ** 3)  # Cubo de impares

objetivo = 1000000
sumaTotal = 0
contador = 0

for numero in numeros:
    if sumaTotal + numero < objetivo:
        sumaTotal += numero
        contador += 1
    else:
        break  

print(f"Suma total: {sumaTotal}")
print(f"Cantidad de números sumados: {contador}")