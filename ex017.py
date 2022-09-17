from math import hypot
x = float(input('Digite a coordenada X do triangulo retangulo: '))
y = float(input('Digite a coordenada Y do triangulo retangulo: '))
h = hypot(x, y)
print('A hipotenusa do Triangulo retangulo de coordenada (X,Y)  ({:.2f},{:.2f}) é {:.2f}'.format(x, y, h))
