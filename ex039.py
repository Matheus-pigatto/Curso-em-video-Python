#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora
# exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

data1 = date.today()
anoatual = date.today().year
data1_ordenada = data1.strftime('%d/%m/%Y')

print('*=*'*10)
print('Alistamento militar')
print('*=*'*10)
print('')
data2 = str(input('Informe a sua data de nascimento \033[1m(dd/mm/aaaa): \033[m'))
print('')
print('*=*'*10)
ndia = int(data2[0:2])                          #vai isolar somente os dias
nmes = int(data2[3:5])                          #vai isolar somente o mes
nano = int(data2[6:10])                         #vai isolar somente o ano
data2 = date(nano,nmes,ndia)                    # transforma a strings em formato data
data2_ordena = data2.strftime('%d/%m/%Y')       #ordenando a data para o formato brasileiro para ficar mais fácil de entender

print('Hoje é dia {} e você nasceu no dia {}'.format(data1_ordenada, data2_ordena))
print('')
dias_alistamento = 6570
difdata = data1-data2
difdata = difdata.days
fdata = (18*365)-difdata


if difdata < 6205:
    print('Você tem menos de 18 anos e faltam {} dias ou {} anos para seu alistamento'.format(fdata,(fdata//365)))
    print('Você deve se alistar em {}'.format(anoatual+(fdata//365)))
elif (difdata > 6205) and (difdata < 6935):
    print('Você tem ou irá fazer 18 anos e deve se alistar esse ano')
else:
    print('Você ja se alistou ou esta com seu alistamento atrasado. \nVocê deveria ter se alistado a {} anos'.format(abs(int(fdata//365))))

