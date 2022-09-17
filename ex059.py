from time import sleep
print('=-=-'*10)
print('Calculadora de operações Básicas'.center(40))
print('=-=-'*10)
n1 = float(input('Digite 1o número: '))
n2 = float(input('Digite 2o número: '))
c = 0
print('=-=-'*10)
while c != 5:
    print('Digite uma das opções a baixo:')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    c = int(input('>>>>>> Opção: '))
    print('=-=-' * 10)
    if c == 1:
        soma = n1+n2
        print('A soma dos valores {} + {} = {} '.format(n1, n2, soma))
        print('Você deseja continuar fazer outra operação [S/N]')
        resposta = str(input()).upper().strip()
        if resposta == 'N':
            c = 5
    elif c==2:
        multiplicação = n1 * n2
        print('A multiplicação dos valores {} * {} = {} '.format(n1, n2, multiplicação))
        print('Você deseja continuar fazer outra operação [S/N]')
        resposta = str(input()).upper().strip()
        if resposta == 'N':
            c = 5
    elif c==3:
        if n1 > n2:
            print('{} é maior {}'.format(n1, n2))
        else:
            print('{} é maior {}'.format(n2, n1))
        print('Você deseja continuar fazer outra operação [S/N]')
        resposta = str(input()).upper().strip()
        if resposta == 'N':
            c = 5
    elif c==4:
        n1 = float(input('Digite 1o número: '))
        n2 = float(input('Digite 2o número: '))
    elif c==5:
        print('Finalizando...')
        sleep(1)
        print('...')
        sleep(1)

    else:
        print('Opção invalida! \nEscolha uma das opções a baixo:')
        print('=-=-' * 10)
print('=-=-' * 10)
print('Obrigado por usar a calculadora'.center(40))