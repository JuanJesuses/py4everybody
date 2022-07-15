""" Hay un cierto número funciones internas que pueden ser utilizadas en las listas que
te permiten mirar rápidamente a través de una lista sin escribir tus propios bucles: """
nums = [3, 41, 12, 9, 74, 15]
print(len(nums)) # la función len devuelve la longitud, en este caso, de una lista

print(max(nums)) # la función max devuelve el valor mayor

print(min(nums)) # la función min devuelve el valor menor

print(sum(nums)) # la función sum devuelve la suma de la lista. Sólo funciona cuando los valores son números.

print(sum(nums) / len(nums))

""" La función sum() solamente funciona cuando los elementos de la lista son números.
Las otras funciones (max(), len(), etc.) funcionan con listas de cadenas y otros
tipos que pueden ser comparados entre sí. """

total = 0
contador = 0
while (True):
    inp = input('Ingresa un número: ')
    if inp == 'fin':
        break
    valor = float(inp)
    total = total + valor
    contador = contador + 1

promedio = total / contador
print('Promedio: ', promedio)

""" En este programa, tenemos las variables contador y total para almacenar la
cantidad y el total actual de los números del usuario según el usuario va ingresando
los números repetidamente.
Podríamos simplemente recordar cada número como el número lo ingresó, y utilizar
funciones internas para calcular la suma y el total de números al final. """

numlista = list() # Mira qué bien, declaración de una lista vacía
while (True):
    inp = input('Introduce un número: ')
    if inp == 'fin':
        break
    valor = float(inp)
    numlista.append(valor)

promedio = sum(numlista) / len(numlista)
print('Promedio: ', promedio)

""" Creamos una lista vacía antes de que comience el bucle, y luego cada vez que
tengamos un número, lo agregamos a la lista. Al final del programa, simplemente
calculamos la suma de los números en la lista y la dividimos por el total de números
en la lista para obtener el promedio. """

