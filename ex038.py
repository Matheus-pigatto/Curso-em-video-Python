#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
print ('*-*-'*10)
print('        Comparador de números')
print ('*-*-'*10)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print ('*-*-'*10)
if n1 > n2:
    print('O número \033[1:31m{}\033[m é maior que \033[1:35m{}\033[m'.format(n1, n2))
elif n2 > n1:
    print('O número \033[1:31m{}\033[m é maior que \033[1:35m{}\033[m'. format(n2, n1))
else:
    print('Não existe valor maior os dois números são \033[1:31mIGUAIS\033[m ')
