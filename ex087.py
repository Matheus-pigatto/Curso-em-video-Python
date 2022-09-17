matriz = [[], [], []]
pares = 0
for x in range(len(matriz)):
    for y in range(0, 3):
        num = int(input(f'Digite um valor para [{x},{y}]: '))
        matriz[x].append(num)
for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        print(f'[{matriz[x][y]:^6}]'.center(6, " "), end=' ')
        if matriz[x][y] % 2 == 0:
            pares += matriz[x][y]
    print()
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {matriz[0][2]+matriz[1][2]+matriz[2][2]}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')