print('+-'*14)
print('ANALIZADOR DE PESSOAS')
print('+-'*14)
nome1 = ''
idade1 = 0
mulher = 0
idadem = 0
cont = 0
print('+-'*10)
for p in range (1, 5):
    nome = str(input('Informe o nome da pessoa: '))
    sexo = str(input('Informe o sexo da pessoa(M/F): ').upper())
    idade = int(input('Informe a idade da pessoa: '))
    print('+-'*10)
    if sexo == 'M' and idade > idade1:
        nome1 = nome
        idade1 = idade
    elif sexo =='F' and idade < 20:
        mulher = mulher + 1
    idadem = idadem + idade
    cont = cont + 1
idadem = idadem/cont
print('O homem mais velhor entre o grupo tem {}anos e se chama: {}'.format(idade1,nome1)
print('No grupo exitem {} mulheres com menos de 20 anos'.format(mulher)))
print('A média da idade do grupo foi de: {}anos'.format(idadem))
