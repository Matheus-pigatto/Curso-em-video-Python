n1 = int(input('Digite o 1o número: '))
n2 = int(input('Digite o 2o número: '))
n3 = int(input('Digite o 3o número: '))
if n1 > n2 and n1 > n3:
    print('O {} é o MIOR número'.format(n1))
else:
    if n2 > n1 and n2 > n3:
        print('O {} é o MAIOR número'.format(n2))
    else:
        print('O {} é o MAIOR número'.format(n3))
if n1 < n2 and n1 < n3:
    print('O {} é o menor número'.format(n1))
else:
    if n2 < n1 and n2 < n3:
        print('O {} é o menor número'.format(n2))
    else:
        print('O {} é o menor número'.format(n3))

