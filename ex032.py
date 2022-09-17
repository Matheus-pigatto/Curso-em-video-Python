# Faça um programa que leia um ano qualquer e diga se ele é bissexto ou não
from datetime import date

ano = int(input('Informe um ano para saber se ele é bissexto: '))
if ano==0:
    ano = date.today().year

bissexto1 = ano%100
bissexto2 = ano%1000
if (bissexto1 % 4 == 0) and (not bissexto1 == 00 ):
    print('O ano {} é um ano bissexto!'.format(ano))
else:
    if (bissexto2 % 400 == 0):
        print('O ano {} é um ano bissexto!'.format(ano))
    else:
        print('O ano {} não é um ano bissexto'.format(ano))
