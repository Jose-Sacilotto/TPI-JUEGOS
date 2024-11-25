import random
def generarmatriz(filas, columnas):
    return [[random.randint(1, 10) for _ in range(columnas)] for _ in range(filas)]
def imprimirmatriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))
def juegosumamatriz():
    filas = 3
    columnas = 3
    matriz = generarmatriz(filas, columnas)
    imprimirmatriz(matriz)
    suma = 0
    for fila in matriz:
        for valor in fila:
            suma += valor
    intento = int(input(f"¿Cuál es la suma de todos los números en la matriz de {filas}x{columnas}? "))
    if intento == suma:
        print("¡Correcto!")
    else:
        print(f"¡Incorrecto! La suma correcta es {suma}. El juego ha terminado.")
juegosumamatriz()