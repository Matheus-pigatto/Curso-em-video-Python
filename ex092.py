import datetime
data = datetime.date.today()
ano = int(data.strftime('%Y'))
cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
cadastro['idade'] = ano - nascimento
cadastro['CTPS'] = int(input('Carteira de Trabalho ( 0 náo tem): '))
if cadastro['CTPS'] != 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = int(input('Salário: R$'))
    anos_trabalhados = int(ano) - cadastro['contratacao']
    if cadastro['idade'] >= 65 or anos_trabalhados >= 15:
        cadastro['aposentadoria'] = 65
    elif cadastro['idade'] >= 65 and anos_trabalhados < 15:
        anos_a_trabalhar = 15 - anos_trabalhados
        cadastro['aposentadoria'] = cadastro['idade'] + anos_a_trabalhar
    elif cadastro['idade'] < 65 and anos_trabalhados < 15:
        idade_a_trabalhar = 65 - cadastro['idade']
        anos_a_trabalhar = 15 - anos_trabalhados
        teste = cadastro['idade'] + anos_a_trabalhar
        if cadastro['idade'] <= 50:
            cadastro['aposentadoria'] = 65
        elif teste <= 65:
            cadastro['aposentadoria'] = 65
        else:
            cadastro['aposentadoria'] = cadastro['idade'] + anos_a_trabalhar
else:
    cadastro['CTPS'] = '(Não tem)'
print('=-'*30)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
