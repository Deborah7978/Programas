# Problema:
# Escribir un programa que proporcione el desglose en el número mínimo de billetes y monedas 
# de una cantidad entera cualquiera de euros dada. Recuerden que los billetes y monedas de uso 
# legal disponibles hasta 1 euro son de: 500, 200, 100, 50, 20, 10, 5, 2 y 1 euros. Para ello 
# deben solicitar al usuario un número entero, debiendo comprobar que así se lo ofrece y desglosar 
# tal cantidad en el número mínimo de billetes y monedas que el programa escribirá finalmente en pantalla.

def main():
    try:
        cantidad = int(input("Introduce una cantidad entera en euros: "))
        if cantidad < 0:
            raise ValueError("La cantidad debe ser no negativa.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    denominaciones = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    cantidad_billetes_monedas = []

    # Desglosar la cantidad en billetes y monedas
    for denom in denominaciones:
        conteo = cantidad // denom
        cantidad_billetes_monedas.append(conteo)
        cantidad -= conteo * denom

    print("Desglose de la cantidad en billetes y monedas:")

    for i in range(len(denominaciones)):
        if cantidad_billetes_monedas[i] > 0:
            print(f"{denominaciones[i]} euros: {cantidad_billetes_monedas[i]} unidades")

if __name__ == "_main_":
    main()