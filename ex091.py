import random
jogadores = dict()
ranking = list()
maior = proximo = 0
for x in range(1, 5):
    dado = random.randint(1, 6)
    jogadores[f'Jogador{x}'] = dado
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
print(f'{"==Ranking dos Jogadores ==":^30} ')
for x in range(1, len(jogadores)+1):
    ranking.append(jogadores[f'Jogador{x}'])
ranking.sort(reverse=True)
#print(ranking)
x = 1
while True:
    position = ranking.index(jogadores[f'Jogador{x}'])
    ranking.pop(position)
    ranking.insert(position, f'Jogador{x}')
    x += 1
    if x > 4:
        break
for x in range(0, 5):
    if x < 4:
        print(f'{x+1}º Lugar: {ranking[x]} com {jogadores[ranking[x]]}')