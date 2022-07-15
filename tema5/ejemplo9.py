def min(valores):
	menor = None
	for valor in valores:
		if menor is None or valor < menor:
			menor = valor
	return menor

n = 0
while n <= 5:
	serie = []
	relleno = int(input('Introduce el número {}: '.format(n)))
	serie.append(relleno)
	n = n +1

print(min(serie))