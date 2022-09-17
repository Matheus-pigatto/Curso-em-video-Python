print('==='*15)
print(f'Lista de produtos'.center(45))
print('==='*15)
tupla_produtos=('Lápis',1.75,
                 'Borracha',2,
                 'Caderno', 15.90,
                 'Estojo', 25,
                 'Transferidor', 4.20,
                 'Mochila', 9.00,
                 'Canetas', 120.21,
                 'Livros',34.90)
for x in range(0,len(tupla_produtos)):
    if x % 2 == 0:
        print(f'{tupla_produtos[x]:.<30}', end='')
    else:
        print(f'R$ {tupla_produtos[x]:>7.2f}')
print('='*45)
