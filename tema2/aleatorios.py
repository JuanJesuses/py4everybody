import random

""" La función random devuelve un número aleatorio entre 0.0 y 1.0
    (incluyendo 0.0 pero NO 1.0) """

for i in range(10):
    x = random.random()
    print(x)

""" La función randint toma los parámetros inferior y superior y devuelve 
    un número entero entre inferior y superior (incluyendo ambos extremos) """

print(random.randint(5, 10))
print(random.randint(5, 10))

# Para elegir un elemento de una secuencia aleatoria, se puede usar choice:

t = [1, 2, 3]
print(random.choice(t))
print(random.choice(t))