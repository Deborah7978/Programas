# Problema:
# Se llama sucesión de Fibonacci a la colección de n números para la que el primer elemento es cero, 
# el segundo 1 y el resto es la suma de los dos anteriores. Por ejemplo, la sucesión para n=5 es (0, 1, 1, 2, 3). 
# Crear un programa que calcule la lista de números para cualquier n.

def calcularSucesionFibonacci(n):
    lista = []

    for i in range(n):
        if i == 0:
            lista.append(0)  # Primer elemento es 0
        elif i == 1:
            lista.append(1)  # Segundo elemento es 1
        else:
            # El resto es la suma de los dos anteriores
            lista.append(lista[i - 1] + lista[i - 2])
 
    return lista

def main():
    while True:
        try:
            n = int(input("Introduce el número de términos de la sucesión de Fibonacci que deseas calcular: "))
            if n < 0:
                print("Por favor, introduce un número entero no negativo.")
                continue

            resultado = calcularSucesionFibonacci(n)
            print(f"La sucesión de Fibonacci para n={n} es: {resultado}")
            break  
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número entero.")


if __name__ == "_main_":
    main()