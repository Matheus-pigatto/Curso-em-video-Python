#Escreva um programa que leia a velocidade um carro caso a velocidade seja maior que 80km/h o carro será multado em R$7,00 por km excedente
v = float(input('Qual é a velocidade atual do carro? '))
multa = (v - 80)*7
if (v > 80):
    print('MULTADO! Vocês excedeu o limite de velocidade permitida de 80km/h \n Você deve pagar uma multa de R${:.2f} !'.format(multa))
else:
    if (v >= 40) and (v < 80):
        print('Você esta dentro do limite de velocidade')
    else:
        print('Vocês esta muito devagar para a velocidade da via')