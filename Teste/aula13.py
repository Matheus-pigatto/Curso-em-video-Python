print('TABUADA')
n = int(input('Qual tabuada você deseja: '))
c = 0
for c in range(0,11):
    tabuada = n * c
    print('{} * {} = {}'.format(n, c, tabuada))

