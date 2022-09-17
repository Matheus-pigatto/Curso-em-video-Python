while True:
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('--' * 20)
    if tabuada < 0:
        break
    for c in range(1,11):
        print(f'{tabuada} X {c:2}  = {tabuada*c}')
    print('--'*20)
print('\033[1m {:^40}\033[m'.format(' PROGRAMA DE TABUADA ENERRADO'))
print('\033[1m{:^40} \033[m'.format('VOLTE SEMPRE'))
print('--'*20)

