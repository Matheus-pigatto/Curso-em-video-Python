salário = float(input('Digite o salário do funcionário: R$ '))
if salário > 1250.00:
    nsalário = salário * 1.10
else:
    nsalário = salário * 1.15
print('O Funcionario que ganhava R${} passa a receber {}'.format(salário, nsalário))
