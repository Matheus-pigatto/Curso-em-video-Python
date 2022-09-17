from datetime import date
print('*-*='*10)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('*-*='*10)
print('')
ctg = {1:'MIRIM',
       2:'INFANTIL',
       3:'JÚNIOR',
       4:'SÊNIOR',
       5:'MASTER'}
print('*-*-*-CATEGORIAS-*-*-*')
print('1- {}\n2- {}\n3- {}\n4- {}\n5- {}\n'.format(ctg[1], ctg[2], ctg[3], ctg[4], ctg[5]))
print('*-*-*-*-'*3)

ano1 = date.today().year
ano2 = int(input('Digite o ano de nascimento do nadador: '))
idade = ano1 - ano2
if idade <= 9:
    print('O nadador possui {} anos e está na categoria: \033[1m{}\033[m'.format(idade, ctg[1]))
elif idade > 9 and idade <= 14:
    print('O nadador possui {} anos e está na categoria: \033[1m{}\033[m'.format(idade, ctg[2]))
elif idade > 14 and idade <= 19:
    print('O nadador possui {} anos e está na categoria: \033[1m{}\033[m'.format(idade, ctg[3]))
elif idade >19 and idade <=25:
    print('O nadador possuir {} anos e está na categoria: \033[1m{}\033[m'.format(idade, ctg[4]))
else:
    print('O nadador possui {} anos e está na categoria: \033[1m{}\033[m'.format(idade, ctg[5]))
print('*-*='*10)