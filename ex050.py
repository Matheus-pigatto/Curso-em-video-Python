t=0
for c in range(0, 6):
    n = int(input('Informe um numero: '))
    if n%2 == 0:
        t = t + n
print('O número a soma dos números pares foi {}'.format(t))