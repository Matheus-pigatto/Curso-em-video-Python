#Exercício Python 071: Crie um programa que simule o
#funcionamento de um caixa eletrônico. No início, pergunte
#ao usuário qual será o valor a ser sacado (número inteiro)
#e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*40)
print('Banco Matheus'.center(40))
print('='*40)
saque = int(input('Qual o valor você quer sacar? R$'))
total = saque
céd = 50
totced = 0
while True:
    if total >= céd:
        total -= céd
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        totced = 0
        if total == 0:
                break