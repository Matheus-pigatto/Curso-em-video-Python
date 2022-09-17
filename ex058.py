import random
import time
n1 = random.randint(0, 10) #Gera um numero aleatorio inteiro de 0-5
contador = 1
print('--=--'*12)
print('=='*10, 'JOGO DE ADIVINHAÇÃO', '=='*10)
print('Para jogar digite um número de [0 - 10] , se esse número for igual\n ao do computador você ganho caso contrario o computador ganhou')
print('--=--'*12)
print('')
n2 = int(input('Qual número você acha que eu pensei: '))
c = n2
while n1 != c:
    if n1 != c:
        print('Você errou, tente novamente!')
        if n1 > c:
            print('Diga um numero maior que {}'.format(c))
        else:
            print('Diga um número menor que {}'.format(c))
        n2 = int(input('Qual número você acha que eu pensei: '))
        c = n2
        contador = contador + 1

print('Parabens! \nVocê ganhou!')
print('Você precisou de {} tentativas!'.format(contador))