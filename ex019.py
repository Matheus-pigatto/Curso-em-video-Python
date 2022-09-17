import random
nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o noem do quarto aluno: '))

n = random.choice([nome1, nome2, nome3, nome4])
print('Aluno sorteado foi {}'.format(n))