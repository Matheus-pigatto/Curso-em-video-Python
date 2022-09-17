import random
print('=-'*26)
print('\033[;1mJogo de par ou impar\033[m'.upper().center(52))
print('=-'*26)
cont = partidas = 0
while True:
    n = int(input('Digite um valor de 0 - 5:'))
    c = random.randint(0, 5)
    resp = ' '
    while resp not in 'PpIi':
        resp = str(input('Par ou Impar? [P/I]: ').upper().strip())
    total = n + c
    par = total % 2
    print('--'*26)
    print(f'Você jogou {n} e o computador jogou {c}. Total foi {total} ', end='')
    print('DEU PAR' if par == 0 else 'DEU IMPAR')
    print('--' * 26)
    if (par == 0 and resp == 'P') or (par != 0 and resp =='I'):
        print('Parabens! VOCÊ GANHOU')
        cont += 1
        partidas += 1
        print('Vamos jogar novamente ...')
    else:
        print('Você perdeu')
        partidas += 1
        break
    print('=-' * 26)
print(f'Você jogou {partidas}x e ganhou {cont}x!')
print('=-' * 26)