import Moeda

numero = float(input('Digite o preço: R$'))
porcentagem = 10
print(f'A metade de {Moeda.moeda(numero)} é {Moeda.moeda(Moeda.metade(numero))}')
print(f'O dobro de {Moeda.moeda(numero)} é {Moeda.moeda(Moeda.dobro(numero))}')
print(f'Aumentado {porcentagem}%, temos {Moeda.moeda(Moeda.aumentar(numero, porcentagem))}')
