lista = []
pares = []
impares =[]
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Não vou adicionar um número repetido.')
    else:
        lista.append(n)
    while True:
        resp = str(input('Quer continuar? [S/N]'))
        if resp not in'SsNn':
            print('Digite uma resposta valida.')
        else:
            break
    if resp in 'nN':
        break
for i, v in enumerate(lista):
    if v%2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('=-'*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de inpares é {impares}')