lista=[]
for x in range(1,6):
    lista.append(int(input(f'Digite o {x}° número ')))
menor=min(lista)
maior=max(lista)
print(f'Você digitou os valores {lista}')
print(f'O menor valor digitado foi {menor} nas posições ', end=' ')
for i, v in enumerate(lista):
    if v==menor:
        print(f'{i}...', end=' ')
print()
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(lista):
    if v==maior:
        print(f'{i}...', end=' ')
print()