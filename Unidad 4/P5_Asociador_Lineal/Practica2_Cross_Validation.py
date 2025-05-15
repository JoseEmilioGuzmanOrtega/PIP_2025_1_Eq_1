#Cross Validation
#No hacerlo con librerias
#Se dividen y al final todos deben de parar por ser de Prueba y de Entrenamiento y al final se saca el promedio de las k generadas
#Valor de False (minimo aceptados son 5) puede ser el que mejor nos convenga con los 60 datos = 10, o 5, etc
import numpy as np
import random as rnd

archivo = open("Instancia_Pokemones.txt")
contenido = archivo.readlines()

X = contenido[3:3 + int(contenido[1])]
X = [i.split("\t") for i in X]
X = [list(map(int, i)) for i in X]

Y = contenido[3 + int(contenido[1]):]
Y = [i.split("\t") for i in Y]
Y = [list(map(int, i)) for i in Y]

X = np.array(X)
Y = np.array(Y)

print("X:")
print(X)
print("Y:")
print(Y)
print("Elementos: ", X.shape)
print("Elementos: ", Y.shape)

k = 10
clases = ["FANTASMA", "HADA", "LUCHA"]
eficiencias = []
tamano_fold = X.shape[1] // k

print("\n#############################################")
print(f"### CROSS MANUAL CON K = {k} FOLDS")
print("#############################################")

for fold in range(k):
    print(f"\n========== Fold {fold + 1} ==========")

    inicio = fold * tamano_fold
    fin = inicio + tamano_fold

    X_prueba = X[:, inicio:fin]
    Y_prueba = Y[:, inicio:fin]

    X_entreno = np.hstack((X[:, :inicio], X[:, fin:]))
    Y_entreno = np.hstack((Y[:, :inicio], Y[:, fin:]))

    # Cálculo de la matriz W
    Paso1 = X_entreno.dot(X_entreno.T)
    Paso2 = np.linalg.inv(Paso1)
    Xpseudo = X_entreno.T.dot(Paso2)
    W = Y_entreno.dot(Xpseudo)

    casosCorrectos = 0

    for i in range(X_prueba.shape[1]):
        print(f"\nPrueba del Caso {i + 1}")
        casoi = X_prueba[:, i]
        print("Caso Analizado:", casoi)

        Ycasoi = W @ casoi
        print("Salidas Generadas:", Ycasoi)

        Yrealcasoi = Y_prueba[:, i]
        print("Salida Real:", Yrealcasoi)

        IndexPred = np.argmax(Ycasoi)
        IndexReal = np.argmax(Yrealcasoi)

        if IndexPred == IndexReal:
            casosCorrectos += 1

        print("Clase Asignada:", clases[IndexPred])
        print("Clase Real:", clases[IndexReal])

    total = X_prueba.shape[1]
    eficiencia = round((casosCorrectos / total) * 100, 2)
    eficiencias.append(eficiencia)
    print(f"\nEficiencia en Fold {fold + 1}: {eficiencia}%")

promedio_eficiencia = round(np.mean(eficiencias), 2)
print("\n#############################################")
print("Resultado final del Cross Validation:")
print("Eficiencias por Fold:", eficiencias)
print("Eficiencia Promedio:", promedio_eficiencia, "%")