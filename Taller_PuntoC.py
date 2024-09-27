import math

def calcular_volumen():
    radio = float(input("Introduce el radio de la esfera: "))
    pi = 3.1416
    volumen = (4/3) * pi * (radio ** 3)
    return volumen

# Ejemplo de uso:
print(f"El volumen de la pelota es {calcular_volumen()}")