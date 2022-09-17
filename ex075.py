lista=[]
cont9 = 0
parlista=[]
for x in range(1, 5):
    y = int(input(f'Digite o {x} º: '))
    lista.append(y)
tupla1 = tuple(lista)
for numero in range(len(tupla1)):
    if tupla1[numero]%2 == 0:
        parlista.append(tupla1[numero])

print(f'O número 9 aparece {tupla1.count(9)}x')
print(f'O número 3 está na {tupla1.index(3)}a posição')
print(f'Os números pares digitados foram {parlista}')
