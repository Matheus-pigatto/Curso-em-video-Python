#n1 = int(input('Digite um numero: '))
#n2 = int(input('Digite outro: '))
#s = n1 + n2
#print('A soma entre {} e {} vale {}'.format(n1, n2, s))


#Faça um programa que leia algo pelo teclado e mostre na tela o tipo primitivo e todas as informações possiveis sobre ele.
n = input('Digite algo: ')
print(type(n))
print('{} é alfanumérico? '.format(n), n.isalnum())
print('{} é um número? ', n.isnumeric())
print('{} é alfabético? ', n.isalpha())
print('{} é digito? ', n.isdigit())
print('O que foi digitado é decimal? ', n.isdecimal())
print('O que foi digitado está em minusculo? ', n.islower())
print('O que foi digitado é imprimivel? ', n.isprintable())
print('O que foi digitado é espaço? ', n.isspace())
print('O que foi digitado está Capitalizada? ', n.istitle())
print('O que foi digitado está em maiusculo? ', n.isupper())
