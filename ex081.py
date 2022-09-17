lista = []
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
print()
print('=-'*30)
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
   print('O valor 5 faz parte da lista!')
else:
   print('O valor 5 não faz parte da lista!')

