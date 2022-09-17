import Moeda
numero = float(input('Digite o preço: R$'))
porcentagem = 10
print(f'A metade de R${numero} é R${Moeda.metade(numero)}')
print(f'O dobro de R${numero} é R${Moeda.dobro(numero)}')
print(f'Aumentado {porcentagem}%, temos R${Moeda.aumentar(numero, porcentagem):.2f}')
