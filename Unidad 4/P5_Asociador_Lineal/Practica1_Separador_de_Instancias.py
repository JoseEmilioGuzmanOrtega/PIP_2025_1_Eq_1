import numpy as np

archivo = open("Instancia_Pokemones.txt")
contenido = archivo.readlines()

X = contenido[3:3+int(contenido[1])]
X = [i.split("\t") for i in X]
X = [list(map(int, i)) for i in X]

Y = contenido[3+int(contenido[1]):]
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

factorEntrenamiento = 0.8

regEntrenamiento = int(factorEntrenamiento * X.shape[1] ) #80% del total de elementos
regPrueba = X.shape[1] - regEntrenamiento

print("Registros para entrenamiento: ", regEntrenamiento)
print("Registros para entrenamiento: ", regPrueba)

posSeleccionadas = []
datosEntrenamientoX = []
datosEntrenamientoY = []

import random as rnd
for i in range(regEntrenamiento):
    index = rnd.randint(0, regEntrenamiento - 1)
    while index in posSeleccionadas:
        index = rnd.randint(0, regEntrenamiento - 1)
    datosEntrenamientoY.append([
        X[0][index],
        X[1][index],
        X[2][index]
    ])
    datosEntrenamientoX.append([
        X[0][index],
        X[1][index],
        X[2][index],
        X[3][index]
    ])
    posSeleccionadas.append(index)
print()

#Asegurar que las 3 clases tengan el 80% de cada clase y tener otro contador que llene si la clase al final fue correctamente llenada
#Split Validation (Este es mas exacto y preciso)

print("\nEvaluación de TODOS los Registros del Conjunto Completo:")

# Cálculo de la matriz W
Paso1 = X.dot(X.T)
Paso2 = np.linalg.inv(Paso1)
Xpseudo = X.T.dot(Paso2)
W = Y.dot(Xpseudo)

# Datos a evaluar
X_eval = X
Y_eval = Y

Clases = ["FANTASMA", "HADA", "LUCHA"]
casosCorrectos = 0

for i in range(X_eval.shape[1]):
    print(f"\nPrueba del Caso {i + 1}")
    casoi = X_eval[:, i]
    print("Caso Analizado:", casoi)

    Ycasoi = W @ casoi
    print("Salidas Generadas:", Ycasoi)

    Yrealcasoi = Y_eval[:, i]
    print("Salida Real:", Yrealcasoi)

    IndexPred = np.argmax(Ycasoi)
    IndexReal = np.argmax(Yrealcasoi)

    if IndexPred == IndexReal:
        casosCorrectos += 1

    print("Clase Asignada:", Clases[IndexPred])
    print("Clase Real:", Clases[IndexReal])

print("\nTotal de Casos Analizados:", X_eval.shape[1])
print("Total de Casos Correctos:", casosCorrectos)
print("Eficiencia del Asociador Lineal:", round(casosCorrectos / X_eval.shape[1] * 100, 2), "%")