def maior(qnt):
    import random, time
    lista = []
    x = 0
    while x < qnt:
        x+=1
        ocorrencias = random.randint(0, 10)
        print('=-'*30)
        for n in range(0, ocorrencias):
            numero = random.randint(0, 10)
            while True:
                if numero not in lista:
                    lista.append(numero)
                    break
                else:
                    numero = random.randint(0, 10)
        print('Analisando os valores passador',end='')
        for tempo in range(0,3):
            time.sleep((0.3))
            print('.', end='')
        print()
        for z in range(0, len(lista)):
            print(f'{lista[z]}', end=" ")
        print(f'Foram informados {len(lista)} valores ao todo.')
        print(f'O maior valor informado foi {max(lista)}.')
        lista.clear()

import random
ocorrencias = random.randint(1, 5)
maior(ocorrencias)