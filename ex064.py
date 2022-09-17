N = n1 = c = cont = 0
while not c == 999:
    N = int(input('Digite um número [999 para parar]: '))
    if N != 999:
        N = N + n1
        n1 = N
        cont += 1
    else:
        c = N
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, n1))