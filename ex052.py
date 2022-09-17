num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[32m{} \033[m'.format(c), end=' ')
        cont = cont + 1
    else:
        print('\033[31m{} \033[m'.format(c), end=' ')
print('')
if cont == 2:
   print('O número {} é primo '.format(num))
    #print(c)
else:
    print('O número {} não é primo'. format(num))
