import time
def maior(* núm): #Parametros empacotados, a função recebe * que representa varios valores.
    cont = maior = 0
    print('=-'*30)
    print('Analisando os valores passados ... ')
    for valor in núm:
        print(f'{valor} ', end="", flush=True)
        time.sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont+=1
    print(f'Foram digitados {cont} valores')
    print(f'O maior valor foi {maior}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()