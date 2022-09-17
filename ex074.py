import random
tupla = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
tupla2 = str(tupla)
tupla2 = tupla2.replace('(', '')
tupla2 = tupla2.replace(',', ' ')
tupla2 = tupla2.replace(')', ' ')
print(f'Os números sorteados foram: {tupla2}')
print(f'O Maior valor sorteado foi {max(tupla)}')
print(f'O Menor valor sorteado foi {min(tupla)}')



