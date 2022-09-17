print('=*=*'*10)
print('Programa para calculo de média')
print('=*=*'*10)
print('')
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2)/2

if m < 5.0:
    print('Sua nota foi \033[1:31m {:.2f}:   ALUNO REPROVADO\033[m'.format(m))
elif m >= 5 and m <= 6.9:
    print('Sua nota foi \033[1:33m{:.2f}: ALUNO EM RECUPERAÇÃO\033[m'.format(m))
elif m > 7 and m <=10:
    print('Sua nota foi \033[1:32m{:.2f}: ALUNO APROVADO\033[m'.format(m))
else:
    print('\033[1:31:40m Verifique as notas digitadas \033[m')
print('=*=*'*10)

