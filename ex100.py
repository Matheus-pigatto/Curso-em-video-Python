import random
def sorteio():
    lista = []
    numero = 0
    print('Sorteando 5 valores da lista:', end='')
    for num in range(0, 5):
        numero = random.randint(0, 10)
        print(f'{numero} ', end="")
        lista.append(numero)
    print('PRONTO!')
    return(lista)
def somapar(lista):
    soma = 0
    for num in lista:
        if num%2 == 0:
            soma+=num
    print(f'Somando os valores pares de {lista}, temos {soma}')
lista1 = []
lista1 = sorteio()
somapar(lista1)

