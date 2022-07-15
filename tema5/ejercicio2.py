""" Ejercicio 2: Escribe otro programa que pida una lista de números como
la anterior y al final muestre por pantalla el máximo y mínimo de los
números, en vez de la media. """

listaNum = list()

def rellenaLista():
    while (True):
        num = input('Introduce un número: ')
        if num == 'fin':
            break
        valor = int(num)
        listaNum.append(valor)
    
    return listaNum
    
def calculaMaximo(listado):
    maximo = 0
    for valor in listado:
        if valor > maximo:
            maximo = valor
    return maximo

def calculaMinimo(listado2):
    minimo = listado2[0]
    for valor in listado2:
        if valor < minimo:
            minimo = valor
    return minimo

lista = rellenaLista()
total = len(lista)

print("El número más alto introducido es: {} y el número más bajo es: {}".format(calculaMaximo(lista), calculaMinimo(lista)))
print('El total de números introducidos es {}.'.format(total))