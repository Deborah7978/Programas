# Problema: 
# Para el cálculo de la letra del DNI se calcula el residuo 23 del número, es decir, el resto que se obtiene 
# de la división entera del número del DNI entre 23. El resultado será siempre un valor entre 0 y 22 y cada 
# uno de ellos tiene asignado una letra según la siguiente tabla:
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
# T R W A G M Y F P D  X  B  N  J  Z  S  Q  V  H  L  C  K  E
# Escribir un programa que solicite el número de DNI al usuario y calcule la letra que le corresponde.

def calcularLetraDNI(dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    residuo = dni % 23
    letra = letras[residuo]
    return letra

def main():
    while True:
        try:
            dni = int(input("Introduce el numero de DNI: "))
            if dni < 0:
                print("Error. Introduce un numero positivo.")
                continue
            break
        except ValueError:
            print("Error. Debe introducir un numero valido.")

    letra = calcularLetraDNI(dni)
    print(f"La letra que corresponde al DNI {dni} es: {letra}")
    
if __name__ == "_main_":
    main()