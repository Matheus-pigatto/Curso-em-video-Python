import pprint
jogador = dict()
golslista = list()
gols_total = 0
jogador['nome'] = str(input('Nome do Jogador: '))
partidas_t = int(input(f'Quantas partidas {nome} jogou? '))
for partida in range(0, partidas_t):
    gols = int(input(f'Quantos gols na partida {partida}? '))
    gols_total = gols_total + gols
    golslista.append(gols)
jogador['gols'] = golslista
jogador['total'] = gols_total
print('=-'*30)
print(jogador)
print('=-'*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f"O jogador {jogador['nome']} jogou {partidas_t}.")
for partidas in range(0, partidas_t):
    print(f'      => Na partida {partidas}, fez {golslista[partidas]} gols.')