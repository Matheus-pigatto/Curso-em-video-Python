import random
import time

jokenpô = {1: 'PEDRA',
           2: 'PAPEL',
           3: 'TESOURA'}
print('*#*#*#'*8)
print('\033[7:31:40m                JOGO DE JOKENPÔ                 \033[m')
print('\033[7:31:40m        Escolha uma das opções a baixo:         \033[m')
print('\033[7:31:40m        [1] - PEDRA                             \033[m')
print('\033[7:31:40m        [2] - PAPEL                             \033[m')
print('\033[7:31:40m        [3] - TESOURA                           \033[m')
print('\033[7:31:40m                                                \033[m')
print('*#*#*#'*8)
opção = (input('Digite a sua jogada: '))
c_opção = random.randint(1, 3)
print('JO...')
time.sleep(1)
print('KEN...')
time.sleep(1)
print('PÔ')
time.sleep(1)
print('')
print('*#*#*#'*8)
if int(opção) == 3 and c_opção == 2:
    print('PARABÉNS! \nVocê escolheu {} \n o computador {}'.format(jokenpô[int(opção)], jokenpô[c_opção]))
elif int(opção) == 2 and c_opção == 1:
    print('PARABÉNS! \nVocê escolheu {} \n o computador {}'.format(jokenpô[int(opção)], jokenpô[c_opção]))
elif int(opção) == 1 and c_opção == 3:
    print('PARABÉNS! \nVocê escolheu {} \n o computador {}'.format(jokenpô[int(opção)], jokenpô[c_opção]))
elif int(opção) == c_opção:
    print('EMPATE! \nVocê escolheu {} \n o computador {}'.format(jokenpô[int(opção)], jokenpô[c_opção]))
elif opção == '':
    print('VOCÊ PERDEU! \nVocê não escolheu {} \n o computador {}'.format('Nada', jokenpô[c_opção]))
elif int(opção) > 3 or int(opção) == 0:
    print('VOCÊ PERDEU! \nVocê não escolheu {} \n o computador {}'.format('Nada', jokenpô[c_opção]))
else:
    print('VOCÊ PERDEU! \nVocê escolheu {} \n o computador {}'.format(jokenpô[int(opção)], jokenpô[c_opção]))
print('*#*#*#' * 8)
