expressao = str(input('Digite a expressão: ' ))
lista=list(expressao)
npe = lista.count('(')
npd = lista.count(')')
if npe == npd:
    print('Sua expressão é valida')
else:
    print('Sua expressão não é valida')

