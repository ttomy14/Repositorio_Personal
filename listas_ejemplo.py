# Crear una lista de 7 números al azar entre el 0 y el 15, que estén ordenados y no repetidos.

import random # Sabemos que vamos a trabajar con números al azar.

lista = []
numero = random.randint(0,15)

while len(lista) < 7:
    if numero not in lista:
        lista.append(numero)
    numero = random.randint(0,15)

lista.sort()
print(lista)

