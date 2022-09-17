import math
print('_'*35)
print('Sequência de Fibonacci'.center(35))
print('_'*35)
N = int(input('Quantos termos você quer mostrar? '))
N = N - 2
n1 = n3 = 0
n2 = 1
print('{} \u21e8 {} \u21e8'.format(n1, n2), end=' ')
while not N == 0:
    N -= 1
    n3 = n1 + n2
    print('{} \u21e8'.format(n3), end=' ')
    n1 = n2
    n2 = n3
print('FIM')
