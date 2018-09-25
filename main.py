from polynomial import polynomial_feature as pf
from tabulate import tabulate
from MyFunctions import *
import matplotlib.pyplot as plt
import numpy as np

# funcion principal
def main():

    tabla = []
    # se pide el grado hasta el cual se quieren hacer las transformaciones
    while True:
        try:
            n = int(input("Digite el grado de la transformacion polinomial deseada: "))
            if n <= 0:
                raise RuntimeError
            break
        except Exception:
            print("Valor inválido")   
    print("\n\n")
    # para cada grado indicado, se hace lo siguiente
    for i in range(1, n+1):
        # lista auxiliar para guardar info para tabular
        tab_aux = []
        # print("-"*50)
        # print("\nGRADO", i)
        tab_aux.append(i)
        # se calculan las 4 matrices con las transformaciones de grado 'i'
        x1, x2, y1, y2 = pf(i)
        # se calculan las thetas del grado 'i'
        vector = regression(x1, y1)
        # se calcula el Error Cuadrático Medio para el conjunto de entrenamiento 
        # y para el conjunto de pruebas
        val1, hx1 = mse(vector, x1, y1)
        val2, hx2 = mse(vector, x2, y2)
        tab_aux.append(val1)
        tab_aux.append(val2)
        # se preparan datos para hacer la grafica
        x1 = x1[:, 1:]
        x2 = x2[:, 1:]
        # se hacen las graficas de cada transformacion
        # plot(x1, hx1)
        # plot(x2, hx2)
        
        tabla.append(tab_aux)
    # se imprime una tabla que resume los errores cuadráticos medios de cada regresion
    
    print(tabulate(tabla, headers=['Degree of the polynomial', 'MSE with train set', 'MSE with test set']))
    
    graf = np.array(tabla)
    
    grado = graf[:, 0]
    error1 = graf[:, 1]
    error2 = graf[:, 2]
    
    plt.plot(grado, error1, 'bo-', label='MSE with train dataset')
    plt.plot(grado, error2, 'ro--', label='MSE with test dataset')
    plt.axis([0, 25, 0.0, 12.0])
    plt.title('Comparison among MSE of train dataset and test dataset')
    plt.xlabel('Degree of the polynomial')
    plt.ylabel('MSE')
    plt.legend(loc=2)
    plt.show()
    

main()
