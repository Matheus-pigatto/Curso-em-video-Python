soma = 0
total = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        total = total + 1
print('A soma total dos {} foi de {}'.format(total, soma))
