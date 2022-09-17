def contador(i, f, p):
    import time
    if i > f:
        if p < 0:
            p*=-1
        print(f'Você quer quer fazer uma contagem de {i} até {f} pulando de {p} em {p}')
        for c in range(i, f-1, -p):
            print(f'{c} ', end='')
            time.sleep(0.2)
        print('FIM!')
    else:
        print(f'Você quer quer fazer uma contagem de {i} até {f} pulando de {p} em {p}')
        for c in range(i, f+1, p):
            print(f'{c} ', end='')
            time.sleep(0.2)
        print('FIM!')
    print('=-' * 20)

#Programa
contador(1, 10, 1)
contador(10, 1, -1)
print('Sua vez!')
i = int(input('Digite o inicio da contagem: '))
f = int(input('Digite o final da contagem: '))
p = int(input('Qual o passo da contagem: '))
contador(i, f, p)


