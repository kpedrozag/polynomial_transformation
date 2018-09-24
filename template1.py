from polynomial import polynomial_feature as pf
from tabulate import tabulate
from MyFunctions import *

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
