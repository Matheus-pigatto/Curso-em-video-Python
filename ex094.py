cadastro = list()
mulheres = list()
cadastrado = dict()
media_idade = 0
while True:
    cadastrado.clear()
    cadastrado['Nome'] = str(input('Nome: ').strip().title())
    while True:
        sexo = str(input('Sexo: [M/F] ').upper().strip())
        if sexo in 'MmfF':
            cadastrado['Sexo'] = sexo
            break
        else:
            print('ERRO! Por Favor, digite apenas M ou F.')
    cadastrado['Idade'] = int(input('Idade: '))
    media_idade += cadastrado['Idade']
    cadastro.append(cadastrado.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N]'))
        if continuar in 'SsNn':
            break
        else:
            print(f'ERRO! Por Favor, digite apenas S ou N.')
    if continuar in 'Nn':
        break
media_idade = media_idade/(len(cadastro))
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
print(f'B) A média de idade é {media_idade:5.2f} anos.')
for m in cadastro:
    if m['Sexo'] in 'Ff':
        mulheres.append(m['Nome'])
print(f'C) A(s) mulheres cadastradas foram {mulheres}.')
print(f'D) Lista das pessoas que estão acima da média:')
for i in cadastro:
    if i['Idade'] >= media_idade:
        print(f"    nome = {i['Nome']};  sexo = {i['Sexo']};  idade = {i['Idade']}")
print('<< ENCERRADO >>')
