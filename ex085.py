lista = [[], []]
for x in range (0, 7):
    numero = int(input(f'Digite o {x+1}º. Valor: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
lista[0].sort(), lista[1].sort()
print(lista)