n = int(input('Digite qual a tabuada será exibida: '))
total = 0
for c in range(0, 11):
    total = n * c
    print('{} x {:2} = {:2}'.format(n, c ,total))
