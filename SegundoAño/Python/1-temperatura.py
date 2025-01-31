# Problema: 
# La variación de temperatura de un cuerpo a temperatura inicial T0T0 en un ambiente a TsTs cambia de la siguiente manera:
# T=Ts+(T0−Ts)  e−ktT=Ts+(T0−Ts)  e−kt
# con t en horas y siendo k un parámetro que depende del cuerpo (usemos k=0.45). Una lata de refresco a 5ºC queda en la guantera 
# del coche a 40ºC. ¿Qué temperatura tendrá 1, 5, 12 y 14 horas? Encontrar las horas que hay que esperar para que el cuerpo esté a 
# 0.5ºC menos que la temperatura ambiente. Definir funciones adecuadas para realizar ambos cálculos para cualquier tiempo y cualquier 
# diferencia de temperatura respecto al ambiente respectivamente.

import math

k = 0.45  

def calcular_temperatura(T0, Ts, t):
    return Ts + (T0 - Ts) * math.exp(-k * t)

def calcular_tiempo_para_temperatura(T0, Ts, deltaT):
    return -math.log((deltaT + Ts - T0) / (Ts - T0)) / k

# Temperaturas iniciales
T0 = 5.0  # Temperatura inicial
Ts = 40.0  # Temperatura ambiente

# Calcular temperaturas para 1, 5, 12 y 14 horas
for t in [1, 5, 12, 14]:
    temperatura = calcular_temperatura(T0, Ts, t)
    print(f'Temperatura después de {t} horas: {temperatura:.2f}ºC')

# Calcular el tiempo para que la temperatura sea 0.5ºC menos que Ts
deltaT = -0.5
tiempo_necesario = calcular_tiempo_para_temperatura(T0, Ts, deltaT)
print(f'Tiempo necesario para que la temperatura sea 0.5ºC menos que {Ts}ºC: {tiempo_necesario:.2f} horas')