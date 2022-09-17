print('+-+-'*8)
print('\033[7:40m        CALCULADORA DE IMC       \033[m')
print('+-+-'*8)
imc = {1 :'Desnutrição Grau V',
       2 : 'Desnutrição Grau IV',
       3 : 'Desnutrição Grau III',
       4 : 'Desnutrição Grau II',
       5 : 'Desnutrição Grau I',
       6 : 'Normal',
       7 : 'Pré-Obesidade',
       8 : 'Obesidade Grau I',
       9 : 'Obesidade Grau II',
       10 : 'Obesidade Grau III'}

altura = float(input('Informe qual a sua altura (m): '))
peso = float(input('Informe qual o seu peso (Kg): '))
IMC = peso / (altura**2)
print('+-+-'*8)
print('Seu IMC é igual a {:.1f} kg/m² que equivale a '.format(IMC), end='')
if IMC < 10:
    print('\033[1m {}\033[m'.format(imc[1]))
elif IMC < 12.9:
    print('\033[1m {}\033[m'.format(imc[2]))
elif IMC <  15.9:
    print('\033[1m {}\033[m'.format(imc[3]))
elif IMC < 16.9:
    print('\033[1m {}\033[m'.format(imc[4]))
elif IMC < 18.4:
    print('\033[1m {}\033[m'.format(imc[5]))
elif IMC < 24.9:
    print('\033[1m {}\033[m'.format(imc[6]))
elif IMC < 29.9:
    print('\033[1m {}\033[m'.format(imc[7]))
elif IMC < 34.5:
    print('\033[1m {}\033[m'.format(imc[8]))
elif IMC < 39.9:
    print('\033[1m {}\033[m'.format(imc[9]))
else :
    print('\033[1m {}\033[m'.format(imc[3]))
