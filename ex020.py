import random
n1 = str(input('Nome do 1o aluno: '))
n2 = str(input('Nome do 20 aluno: '))
n3 = str(input('Nome do 3o aluno: '))
n4 = str(input('nome do 4o aluno: '))
lista = [n1, n2, n3,n4]
random.shuffle(lista)
print('A ordem de apresentação dos alunos será',lista)
