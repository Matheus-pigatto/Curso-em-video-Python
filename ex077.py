palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIZ','ESTUDAR','PRATICAR')
vogais = ('A','E','I','O','U')
for x in palavras:
    print(f'Na palavra {x} temos as vogais: ',end='')
    for v in vogais:
        if v in x:
            print(v.lower(),end=' ')
    print('')