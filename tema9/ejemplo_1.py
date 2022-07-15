# Crear un diccionario vacío
eng2sp = dict()
print(eng2sp)

# Para añadir elementos a un diccionario se pueden utilizar corchetes
eng2sp['one'] = 'uno'
print(eng2sp)

# Creamos un diccionario con tres elementos y puede ser que no los muestre ordenados, ya que para localizar un elemento se utiliza su clave
eng2sp = {'one' : 'uno', 'two' : 'dos', 'three' : 'tres'}
print(eng2sp)

# La clave 'two' siempre se asocia al valor 'dos', así que el orden de los elementos no importa
print(eng2sp['two'])

# Si la clave no está en el diccionario se obtiene una excepción (exception):
# print(eng2sp['four'])

# La función 'len' funciona en diccionarios, devolviendo el número de pares clave-valor
print(len(eng2sp))

# Operador 'in'. Muestra si algo aparece como una clave en el diccionario (aparecer como valor no es suficiente)
print('one' in eng2sp)
print('uno' in eng2sp)

# El método 'values' devuelve los valores como una lista, así sabremos si algo aparece como valor en un diccionario
valores = list(eng2sp.values())
print('uno' in valores)
print(valores)
