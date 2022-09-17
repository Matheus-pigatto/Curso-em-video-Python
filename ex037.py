print('\033[1:34m-=-\033[m'*20)
print('\033[1:30:44m                Conversor de base numérica                 \033[m ')
print('\033[1:34m-=-\033[m'*20)
print('')
n = int(input('Digite o número no qual deseja converter sua base numérica: '))
he = hex(n)
oc = oct(n)
bi = bin(n)
print('')
print('Escolhas uma das opçoes a baixo')
print('1 - Para converter para base binária')
print('2 - Para converter para base octal')
print('3 - Para converter para base hexadecimal')
print('4 - Para converter para todas as opções')
opção = int(input())
print('')
if opção == 1:
    print('O valor {} convertido para a base binaria é {}'.format(n, bi[2:]))
elif opção == 2:
    print('O valor {} convertido para a base octal é {}'.format(n, oc[2:]))
elif opção == 3:
    print('O valor {} convertido para a base hexadecimal é {}'.format(n, he[2:]))
elif opção == 4:
    print('O valor {} convertido para a base binaria é: {}'.format(n, bi[2:]))
    print('O valor {} convertido para a base octal é: {}'.format(n, oc[2:]))
    print('O valor {} convertido para a base hexadecimal é: {}'.format(n, he[2:]))
else:
    print('Digite uma opção valida')
print('\033[1:34m-=-\033[m'*20)
print('\033[1:30:44m                           OBRIGADO                           \033[m ')
print('\033[1:34m-=-\033[m'*20)

