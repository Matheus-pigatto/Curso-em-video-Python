import Moeda

numero = float(input('Digite o preço: R$'))
porcentagem = 10
print(f'A metade de {Moeda.moeda(numero)} é {Moeda.metade(numero, False)}')
print(f'O dobro de {Moeda.moeda(numero)} é {Moeda.dobro(numero, True)}')
print(f'Aumentado {porcentagem}%, temos {Moeda.aumentar(numero, porcentagem, True)}')
