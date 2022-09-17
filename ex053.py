a = 'DETECTOR DE PALINDROMO'
print('*-'*25)
print(a.center(50))
print('*-'*25)
print()

frase = str(input('Digite uma frase: ').strip().lower())
fraseorig = frase
tfraseorig = len(fraseorig)
frase = frase.replace(" ", "")
nova_frase = frase[::-1]

print()

if nova_frase == frase:
    print('\033[31mA frase digitada é um palíndromo!\033[m')
else:
    print('\033[31mA frase digitada não é um palíndromo!\033[m')
print()

for c in range(0, tfraseorig):
    x = fraseorig[c]
    if x.isspace() == True:
        nova_frase = nova_frase[:c] + ' ' + nova_frase[c:]


print('A frase digitada foi: \n{}'.format(fraseorig))
print()
print('A frase invertida foi: \n{} '.format(nova_frase))

