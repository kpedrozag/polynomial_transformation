import numpy as np
import matplotlib.pyplot as plt

# funcion que calcula el Error Cuadrático Medio
# y retorna ademas un array de predicciones
def mse(theta, data_x, data_y):
    val = 0
    data_hx = []
    for i in range(data_y.shape[0]):
        hx = 0
        for j in range(theta.shape[0]):
            hx += (theta[j] * data_x[i][j])
        data_hx.append(hx)
        val += (hx - data_y[i])**2
    val = (val / data_y.shape[0])
    return val, np.array(data_hx)

# Funcion que realiza el calculo del vector Theta 
# con base en la formula de Ecuaciones Normales
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

"""
def show_vector(vector):
    for j in range(vector.shape[0]):
        if j != 0:
            print(str(vector[j]) + 'x' + str(j), end=' ')
        else:
            print(str(vector[j]), end=' ')
        if j+1 != vector.shape[0]:
            print('+', end=' ')
"""
# Grafica de las predicciones
def plot(X, y):
    plt.plot(X, y, "b.")
    plt.axis([-3, 3, 0, 10])
    plt.show()
