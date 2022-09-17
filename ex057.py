masculino = 0
feminino = 0
c = str('0')
while c != 'N':
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper().strip()
    if sexo == 'M' or sexo == 'F':
        if sexo == 'M':
            masculino = masculino + 1
        else:
            feminino = feminino + 1
        c = str(input('Deseja continuar? [S/N]')).upper().strip()

    else:
        print('Digite uma opção valida.')

print('Você digitou:\n - {} pessoas do sexo masculino \n - {} pessoas do sexo finino'.format(masculino,feminino))


