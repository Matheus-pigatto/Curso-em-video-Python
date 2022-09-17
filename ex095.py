jogador = dict()
jogadores = list()
golslista = list()
gols_total = 0
chaves = list()
while True:
    jogador.clear()
    golslista.clear()
    gols_total = 0
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas_t = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for partida in range(0, partidas_t):
        gols = int(input(f'Quantos gols na partida {partida+1}? '))
        gols_total += gols
        golslista.append(gols)
    jogador['gols'] = golslista[:]
    jogador['total'] = gols_total
    jogadores.append(jogador.copy())
    while True:
        resp = str(input(f'Quer continuar? [S/N]').upper().strip())
        if resp not in 'NnSs':
            print(f'\033[1;31m ERRO! Digite uma resposta valida!!\033[0;0m')
        else:
            break
    if resp in 'Nn':
        break
for x in jogador.keys():
    chaves.append(x)
print('=-'*30)
print(f'cod ', end='')
for i in jogador.keys():
    print(f'{i:<19}',end='')
print()
print(f'-'*60)
for k, v in enumerate(jogadores):
    print(f'{k:>3}', end=" ")
    for d in v.values():
        print(f"{str(d):<19}", end='')
    print()
print(f'-'*60)
while True:
    pesquisa = int(input('Mostrar dados de qual jogador?(999 para parar)'))
    if pesquisa < len(jogadores):
        print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[pesquisa]['nome']}:")
        for partidas in range(0, len(jogadores[pesquisa]['gols'])):
            print(f"      => No jogo {partidas+1}, fez {jogadores[pesquisa]['gols'][partidas]} gols.")
    elif pesquisa == 999:
        break
    else:
        print(f'\033[1;31m ERRO! Digite um numero valido!!\033[0;0m')


