#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np


def polynomial_feature(degree):
    dataSet = np.loadtxt("ex2data1.txt", delimiter=',')

    sixty = int(dataSet.shape[0] * 0.6)

    X = dataSet[:, 0]
    changes = []

    if degree >= 2:
        for i in range(1, degree):
            aux = np.array(0)
            for value in X:
                aux = np.append(aux, np.power(value, i+1))
            aux = np.delete(aux, 0)
            changes.append(aux)
        for i in changes:
            X = np.c_[X, i]
    X = np.c_[np.ones(dataSet.shape[0]), X]

    x_train = X[:sixty]
    x_test = X[sixty:]

    y_train = dataSet[:sixty, 1]
    y_test = dataSet[sixty:, 1]

    return x_train, x_test, y_train, y_test
