print("=================================")
print('Os 10 primeiro termos da PA')
print("=================================")
a1 = int (input('Informe qual será o primeiro termo da PA: '))
r = int(input('Digite qual a razão da PA: '))
c = 1
while c <= 10:
    an = a1 + (c - 1)*r
    print('{}'.format(an), end=' -> ')
    c += 1
print('ACABOU')
# an = a1 + (n - 1).r
