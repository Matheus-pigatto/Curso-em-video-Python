cont = 'S'
Maior = Menor = contador = somátorio = 0
while cont == 'S':
    N = int(input('Digite um número: '))
    if N > Maior:
        Maior = N
    else:
        if Menor == 0:
            Menor = N
        if N < Menor:
            Menor = N
    contador = contador + 1
    somátorio = N + somátorio
    cont = str(input('Deseja continuar? [S/N]: ').upper().lstrip())
média = float((somátorio / contador))
print('Você digitou {} números e a média foi {}.'
      '\nO maior valor foi {} e o menor foi {}'.format(contador, média, Maior, Menor))
print('Acabou!')