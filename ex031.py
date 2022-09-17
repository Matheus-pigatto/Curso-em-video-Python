# Calcular o preço de uma passagem de acordo com o km percorrido
# R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas
custo1 = 0.45
custo2 = 0.50
distancia = float(input('Digite o a distância total da viagem que você irá fazer: '))
if (distancia > 200):
    preco = distancia*custo1
    print('Você irá percorrer {}Km e pagará {}/km percorrido, totalizando em um custo de R${:.2f} '.format(distancia,custo1,preco))
else:
    preco = distancia*custo2
    print('Você irá percorrer {}Km e pagará {}/km percorrido, totalizando em um custo de R${:.2f} '.format(distancia,custo2,preco))