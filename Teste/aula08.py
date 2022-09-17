import math

num = float(input('Digite um número real: '))

print('O numero {} arredondado corresponde a'.format(num), math.trunc(num))
print('Seu arredondadomento para cima corresponde a',math.ceil(num))
print('Seu arredondadomento para baixo corresponde a',math.floor(num))


