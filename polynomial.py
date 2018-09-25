#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

# Funcion que recibe un entero como grado de la transformacion polinomial
def polynomial_feature(degree):
    # se cargan los datos
    dataSet = np.loadtxt("ex2data1.txt", delimiter=',')
    # se calcula la cantidad de datos pertenecientes al 60%
    sixty = int(dataSet.shape[0] * 0.6)

    # features
    X = dataSet[:, 0]
    # acumula los arrays de las transformaciones de X
    changes = []

    # siendo la transformacion con grado mayor o igual a 2
    if degree >= 2:
        # para cada transformacion, se eleva al grado indicado el array X
        for i in range(1, degree):
            changes.append(np.power(X, i+1))
        # se concatenan los cambios a X
        for i in changes:
            X = np.c_[X, i]
    # se concatena la columna de 1's
    X = np.c_[np.ones(dataSet.shape[0]), X]

    # se hace la division del 60% (para entrenar el modelo) y 40% (para hacer pruebas)
    x_train = X[:sixty]
    x_test = X[sixty:]

    y_train = dataSet[:sixty, 1]
    y_test = dataSet[sixty:, 1]
    
       

    return x_train, x_test, y_train, y_test
