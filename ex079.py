lista=[]
while True:
    x = int(input('Digite um valor: '))
    if x in lista:
        print('Valor duplicado. Não vou adicionar....')
    else:
        lista.append(x)
    while True:
        continuar = str(input('Quer Continuar?[S/N]')).upper().strip()
        if continuar in 'SsNn':
            break
        else:
            print('Digite uma resposta valia!')
    if continuar == 'N':
        break
print(f'=-'*30)
lista.sort()
print(lista)




