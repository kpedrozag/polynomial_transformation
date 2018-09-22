import numpy as np
import matplotlib.pyplot as plt
from polynomial import polynomial_feature as pf
from tabulate import tabulate


def mape(theta, data_x, data_y):
    val = 0
    for i in range(data_y.shape[0]):
        hx = 0
        for j in range(theta.shape[0]):
            hx += (theta[j] * data_x[i][j])
        val += (abs(data_y[i] - hx) / data_y[i])
    val = (val / data_y.shape[0]) * 100

    #print("MAPE es:", val, "% de error.")
    return val
    

def regression(x, y):
    X = np.matrix(x)
    Y = np.matrix(y)

    theta = X.T * X
    theta = theta.I
    theta = theta * X.T
    theta = theta * Y.T

    theta = np.array(np.array(theta.T)[0])

    return theta


def get_values():
    dataSet = np.loadtxt("ex2data1.txt", delimiter=',')
    # X = dataSet[:, 0]
    y = dataSet[:, 1]
    return y


def show_vector(vector):
    for j in range(vector.shape[0]):
        if j != 0:
            print(str(vector[j]) + 'x' + str(j), end=' ')
        else:
            print(str(vector[j]), end=' ')
        if j+1 != vector.shape[0]:
            print('+', end=' ')


def main():

    tabla = []

    for i in range(1, 20):
        tab_aux = []
        #print("\nGRADO", i)
        tab_aux.append(i)
        x1, x2, y1, y2 = pf(i)
        vector = regression(x1, y1)
        # show_vector(vector)
        #print("\nANALISIS DE h(x) GRADO ", i)
        tab_aux.append(mape(vector, x1, y1))
        tab_aux.append(mape(vector, x2, y2))
        tabla.append(tab_aux)
    print(tabulate(tabla, headers=['Grado del polinomio', 'MAPE con train set (%)', 'MAPE con test set (%)']))


def plot(X, y):
    #Plotting data
    plt.plot(X, y, "b.")
    plt.axis([-3, 3, 0, 10])
    plt.show()

main()
