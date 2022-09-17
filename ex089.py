alunos = []
alunotemp = []
cores = {'limpa': '\033[m',
         'negrito': '\033[1m',
        'verde': '\033[32m',
         'amarelo': '\033[1:33m',
         'vermelho': '\033[1:31m',
         'cian': '\033[1:36m'}
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2)/2
    alunotemp.append(nome)
    alunotemp.append(nota1)
    alunotemp.append(nota2)
    alunotemp.append(media)
    alunos.append(alunotemp[:])
    alunotemp.clear()
    resp = str(input('Quer continuar? [S/N]').upper().strip())
    if resp in 'nN':
        break
print('=-=-'*20)
print('No.  NOME           MÉDIA')
print('-'*50)
for i, a in enumerate(alunos):

    print(f'{cores["negrito"]}{i:<5}{cores["limpa"]}', end='')
    print(f'{cores["negrito"]}{a[0]:<15}{cores["limpa"]}', end='')
    if a[3] > 6:
        print(f'{cores["verde"]}{a[3]:<5}{cores["limpa"]}')
    else:
        print(f'{cores["vermelho"]}{a[3]:<5}{cores["limpa"]}')
print('-'*50)
while True:
    naluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print('-'*50)
    if naluno == 999:
        print(f'{cores["negrito"]}Volte sempre, OBRIGADO!')
        break
    print(f'Notas de {cores["vermelho"]}{alunos[naluno][0]}{cores["limpa"]} são {cores["cian"]}{alunos[naluno][1:3]}{cores["limpa"]}')
    print('-'*50)

