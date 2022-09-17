#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal
# não pode exceder 30% do salário ou então o empréstimo será negado.
cores = {'limpa': '\033[m',
         'negrito': '\033[1m',
        'verde': '\033[32m',
         'amarelo': '\033[1:33m',
         'vermelho': '\033[1:31m',
         'cian': '\033[1:36m'}

print('\033[1:34m-=-\033[m'*20)
print('\033[1m \033[7:40m             Programa para aprovação de emprestimo           \033[m')
print('\033[1:34m-=-\033[m'*20)

casa = float(input('Digite o valor do imóvel que deseja comprar: R$'))
salário: float = float(input('Informe qual foi o valor do seu ultimo salário: R$'))
anos = int(input('Informe em quantos anos você pretende finalizar o financiamento: '))
prestação = casa/(anos*12)
psalario = 0.3*salário

print('\033[1:34m-=-\033[m'*20)
print('\033[1m \033[7:40m                                                             \033[m')
print('\033[1:34m-=-\033[m'*20)

if psalario >= prestação:
    print('{}Seu financiamento é possivel. Parabens! {}'.format(cores['negrito'],cores['limpa']))
    print('Para financiar um imóvel de {}R${:.2f}{}, você pagará uma prestação de {}R${:.2f}{} mensais pelos proximos {}{} anos{}'.format(cores['amarelo'], casa, cores['limpa'],cores['vermelho'], prestação, cores['limpa'],cores['cian'], anos, cores['limpa'],))
else:
    print('Seu financiamento não foi aprovado.\nTente fazer um financiamento mais longo ou verifique um imóvel mais barato.')

