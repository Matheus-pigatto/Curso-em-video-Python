def area(l, c):
    #programa para calculo de área de um terreno
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}m2')
    return a

#Programa Principal
print('-'*30)
print(f'{"Controle de Terrenos":^30}')
print('-'*30)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m) '))
area(largura, comprimento)
