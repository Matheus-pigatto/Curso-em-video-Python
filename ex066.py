A = cont = soma = 0
while True:
    A = int(input('Digite um valor (999 para sair): '))
    if A == 999:
        break
    cont += 1
    soma += A
print(f'Foram digitados {cont} números e a soma entre eles foi de {soma}!')
