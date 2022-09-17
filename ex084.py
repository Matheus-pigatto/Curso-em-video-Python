lista_pessoas = []
lista_cadastro = []
maior = menor = cont = 0
lista_maior = []
lista_menor = []
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    lista_cadastro.append(nome)
    lista_cadastro.append(peso)
    lista_pessoas.append(lista_cadastro[:])
    if cont == 0:
        maior = peso
        menor = peso
        lista_maior.append(lista_cadastro[:])
        lista_menor.append(lista_cadastro[:])
    else:
        if peso > maior:
            lista_maior.clear()
            maior = peso
            lista_maior.append(lista_cadastro[:])
        elif peso == maior:
            maior = peso
            lista_maior.append(lista_cadastro[:])
        elif peso < menor:
            lista_menor.clear()
            menor = peso
            lista_menor.append(lista_cadastro[:])
        elif peso == menor:
            menor = peso
            lista_menor.append(lista_cadastro[:])
    lista_cadastro.clear()
    cont += 1
    resp = str(input('Quer Continuar? [S/N]'.strip().upper()))
    if resp in 'nN':
        break
print('=-'*30)
print(f'Ao todo, você cadastrou {len(lista_pessoas)} pessoa.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for i, v in enumerate(lista_maior):
    print(lista_maior[i][0], end=', ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for i, v in enumerate(lista_menor):
    print(lista_menor[i][0], end=', ')
