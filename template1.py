import numpy as np
import matplotlib.pyplot as plt
from polynomial import polynomial_feature as pf
from tabulate import tabulate


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


def plot(X, y):
    plt.plot(X, y, "b.")
    plt.axis([-3, 3, 0, 10])
    plt.show()


def main():

    tabla = []
    while True:
        try:
            n = int(input("Digite el grado de la transformacion polinomial deseada: "))
            if n <= 0:
                raise RuntimeError
            break
        except Exception:
            print("Valor inválido")            
    
    for i in range(1, n+1):
        tab_aux = []
        print("-"*50)
        print("\nGRADO", i)
        tab_aux.append(i)
        x1, x2, y1, y2 = pf(i)
        vector = regression(x1, y1)
        # show_vector(vector)
        #print("\nANALISIS DE h(x) GRADO ", i)
        val1, hx1 = mse(vector, x1, y1)
        val2, hx2 = mse(vector, x2, y2)
        tab_aux.append(val1)
        tab_aux.append(val2)
        
        x1 = x1[:, 1:]
        x2 = x2[:, 1:]
        
        plot(x1, hx1)
        plot(x2, hx2)
        
        tabla.append(tab_aux)
    print(tabulate(tabla, headers=['Grado del polinomio', 'MSE con train set', 'MSE con test set']))

main()
