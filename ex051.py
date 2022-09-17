print("=================================")
print('Os 10 primeiro termos da PA')
print("=================================")
a1 = int (input('Informe qual será o primeiro termo da PA: '))
r = int(input('Digite qual a razão da PA: '))
for n in range (1, 11):
    an = a1 + (n - 1)*r
    print('{}'.format(an), end=' -> ')
print('ACABOU')
# an = a1 + (n - 1).r
