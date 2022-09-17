print('-'*40)
print('LOJA SUPER BARATÃO'.center(40))
print('-'*40)
total = m_1000 = barato =0
produto_barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    if preço >= 1000:
        m_1000+=1
    if barato == 0:
        barato = preço
    else:
        if barato > preço:
            barato = preço
            produto_barato = produto
    conti = str(input('Quer continuar?[S/N]: ').upper().strip())
    while conti not in 'SsnN':
        conti = str(input('Quer continuar?[S/N]: ').upper().strip())
    if conti == 'N':
        break
    print('-' * 40)
print(f'O total gasto na compra foi de R${total:.2f} foram comprados {m_1000} produtos com preço maior que R$1,000.00 \n e o produto mais barato foi o(a) {produto_barato} com o valor de R${barato:.2f}. ')