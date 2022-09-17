print('+-+-'*20)
print('Calculadora de fatorial'.center(80))
c = int(input('Digite o número que você deseja saber o fatorial: '))
f = 1
print('{}! = '.format(c), end='')
while c > 0:
    f = f * c
    print(c if c > 0 else '', end='')
    print(' x ' if c > 1 else '', end='')
    c = c - 1
print(' =',f)



