from random import randint
from time import sleep
from operator import itemgetter
jogo = ranking = dict()
dado = 0
for x in range(0,4 ):
    dado = randint(1, 6)
    jogo[f'Jogador{x}'] = dado
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{"==Ranking dos Jogadores ==":^30} ')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
