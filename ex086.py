matriz = [[], [], []]
for x in range(len(matriz)):
    for y in range(0, 3):
        num = int(input(f'Digite um valor para [{x},{y}]: '))
        matriz[x].append(num)
for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        print(f'[{matriz[x][y]:^6}]'.center(6, " "), end=' ')
    print()
