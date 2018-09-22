from tabulate import tabulate
lista = []

for i in range(3):
    aux = []
    for j in range(4):
        aux.append(str(i) + ',' + str(j))
    lista.append(aux)

print(tabulate(lista, headers=), )
