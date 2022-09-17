homem = mulheres = idade = c_idade = m_menor = 0
sexo = cont = ' '
print('-'*30)
print('CADASTRE UMA PESSOA'.center(30))
print('-'*30)
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ').upper().strip())
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ').upper().strip())
    if idade >= 18:
        c_idade +=1
    if sexo == 'F' and idade < 18:
        m_menor +=1
    if sexo == 'M':
        homem+=1
    print('-' * 30)
    cont = str(input('Quer continuar [S/N]').upper().strip())
    while cont not in 'SsnN':
        cont = str(input('Quer continuar [S/N]').upper().strip())
    if cont == 'N':
        break
    print('-' * 30)
print(f'Foram cadastradas {c_idade} pessoas maior(es) de 18 anos.')
print(f'Foram cadastradas {m_menor} mulher(es) menor(es) de 20 anos.')
print(f'Foram cadastrados {homem} homen(s).')

