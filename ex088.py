from random import sample
from time import sleep
listajogos = []
print('-'*30)
print('JOGA NA MEGA SENA')
print('-'*30)
n = int(input('Quantos jogos você quer jogar: '))
for y in range(1, 61):
    listajogos.append(y)
for x in range(1, n):
    print(f'Jogo {x}: {sorted(sample(listajogos, k= 6))}')
    sleep(1)