def ficha(nome='<Desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
#programa principal
nome = str(input('Nome do Jogador: '))
gol = input('Número de Gols: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip()=="":
    ficha(gols=gol)
else:
    ficha(nome, gol)
