leve = 0
pesado = 0
for c in range(1, 6):
    peso = float(input('Informe o peso de da pessoa (Kg): '))
    if c == 1:
        leve = peso
        pesado = peso
    else:
        if peso > pesado:
            pesado = peso
        elif peso < leve:
            leve = peso
print('Pessoa mais pesada pesa {:.2f}Kg e a mais leve pesa {:.2f}Kg'.format(pesado, leve))
