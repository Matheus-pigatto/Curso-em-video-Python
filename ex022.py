nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e tem {} letras'.format(dividido[0],len(dividido[0])))
# pode usar o nome.count(' ') para contar o espaço vazio ou criar uma variavel para contagem do nome vazio e fazer a subtração por essa contagem