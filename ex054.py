from datetime import date
maioridade = 0
menoridade = 0
ano = date.today().year
for c in range (a, b):
    data_nascimento = (input('Digite o ano do nascimento da {}ª pessoa: '.format(c)))
    if len(data_nascimento) == 4:
         idade = ano - int(data_nascimento)
         if idade => 21:
                 maioridade = maioridade +1
         else:
                 menoridade += 1

print('Das 7 pessoas informadas \033[32m{}\033[m são maiores de idade e \033[32m{}\033[m são menores de idade'.format(maioridade,menoridade))