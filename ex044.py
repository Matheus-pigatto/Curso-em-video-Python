preço = float(input('Informe o preço do produto comprado: R$ '))
print('Escolha uma das opções de pagamento a baixo')
print('[1] - á vista dinheiro/cheque: 10% de desconto')
print('[2] - á vista no cartão: 5% de desconto')
print('[3] - em até 2x no cartão: preço formal')
print('[4] - 3x ou mais no cartão: 20% de juros')
opção= int(input('Opção desejada: '))
if opção == 1:
    total = preço * 0.9
    print('Valor do produto é R${:.2f} com 10% de desconto: R${:.2f}'.format(preço, total))

elif opção == 2:
    total = preço * 0.95
    print('Valor do produto é R${:.2f} com 5% de desconto: R${:.2f}'.format(preço, total))
elif opção == 3:
    total = preço/2
    print('Valor do produto é R${:.2f} em 2x de: R${:.2f}'.format(preço, total))

elif opção == 4:
    parcela = int(input('Informe o número de parcelas 3 ou mais: '))
    total = (preço*1.2)
    valor_parcela = total/parcela
    print('Valor do produto é R${:.2f} em {}x de : R${:.2f}, total: R${:.2f} '.format(preço, parcela, valor_parcela, total ))
else:
    print('Digite uma opção valida')

