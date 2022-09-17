print("=================================")
print('Os 10 primeiro termos da PA')
print("=================================")
a1 = int(input('Informe qual será o primeiro termo da PA: '))
r = int(input('Digite qual a razão da PA: '))
c = 1
d = 10
total = d
while not d == 0:
    while c <= total:
            an = a1 + (c - 1) * r
            print('{}'.format(an), end=' -> ')
            c += 1
    print('Pausa')
    d = int(input('Quantos termos você quer mostrar a mais? '))
    total = total + d
print('Obrigado por usaro o Gerador de PA. A progressão utilizou {} termos'.format(c-1))
# an = a1 + (n - 1).r
