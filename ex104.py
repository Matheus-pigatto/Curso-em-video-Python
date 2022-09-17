def leiaint(msg):
    print('--'*20)
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mErro Digite um número inteiro válido\033[m ')
            continue
        else:
            return n

        
def leiafloat(msg):
    print('---'*20)
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mErro Digite um número inteiro válido\033[m ')
            continue
        else:
            return n


#Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
n = leiafloat('Digite um número Real: ')
print(f'Você acabou de digitar o número {n}')
