import sistema.cores as c
import time


def menu(msg):
    time.sleep(0.3)
    print('-' * 35)
    print(c.cor('2'), f'{msg:^35}', c.cor(0))
    print('-' * 35)


def itens(lista):
    cont=1
    for item in lista:
        time.sleep(0.3)
        print(f'{c.cor(1)} {cont} {c.cor(0)} - {c.cor(3)} {item} {c.cor(0)}')
        cont+=1


def opcao(item):
    time.sleep(0.3)
    print('-' * 35)
    print(c.cor('2'), f'Opeção {item}'.center(30), c.cor(0))
    print('-' * 35)


