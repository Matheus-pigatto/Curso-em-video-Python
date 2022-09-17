preço = float(input('Qual o preço do produto? R$ '))
desc = preço*0.95
print('O poduto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, desc))