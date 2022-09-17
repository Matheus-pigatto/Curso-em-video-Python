import random
import time
n1 = random.randint(0, 5) #Gera um numero aleatorio inteiro de 0-5
print('--=--'*12)
print('=='*10, 'JOGO DE ADIVINHAÇÃO', '=='*10)
print('Para jogar escolha digite um número, se esse número for igual\n ao do computador você ganho caso contrario o computador ganhou')
print('--=--'*12)
print('')
n2 = int(input('Qual número você acha que eu pensei: '))
print('...')
time.sleep(2)
print('...')
time.sleep(2)
print('...')
time.sleep(2)
if n2==n1:
    print('Parabens! \nVocê ganhou!')
else:
    print('Vocês perdeu. Eu pensei no número {} e você {}. \nTente de novo.'.format(n1,n2))
