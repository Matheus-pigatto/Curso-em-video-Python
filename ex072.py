numero = (0,'Zero', 1, 'Um', 2, 'Dois', 3, 'Três', 4, 'Quatro', 5,
          'Cinco', 6, 'Seis', 7, 'Sete', 8, 'Oito', 9, 'Nove', 10, 'Dez', 11, 'Onze', 12 ,
          'Doze', 13, 'Treze', 14, 'Quatorze', 15, 'Quinze', 16,  'Dezesseis', 17, 'Dezessete',
          18, 'Dezoito', 19, 'Dezenove', 20, 'Vinte')
continua = 'S'
n = int(input('Digite um numero entre 0 - 20: '))
while True:
    while n not in numero:
        print('Tente Novamente.', end= ' ')
        n = int(input('Digite um número entre 0 - 20: '))
    pos = numero.index(n) + 1
    print(f'Você digitou o número {numero[pos]}')
    continua = str(input('Quer continuar? [S/N]'))
    if continua in 'Nn':
        break
    n = int(input('Digite um número entre 0 - 20: '))
print('Obrigado!')