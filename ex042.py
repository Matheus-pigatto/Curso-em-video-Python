import math

l1 = float(input('Digite o primeiro lado do triangulo: ')) #a
l2 = float(input('Digite o segundo lado do triangulo: ')) #b
l3 = float(input('Digite o terceiro lado do triangulo: ')) #c
m1 = math.fabs(l2 - l3)
m2 = math.fabs(l1 - l3)
m3 = math.fabs(l1 - l2)
print('-=-'*30)
print('Para que 3 retas formem um triângulo elas, devem satisvazer a condição: ')
print("""| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b""")
print('-=-'*30)
print('a = {}, b = {}, c = {}'.format(l1, l2, l3))
print('')
print('{} < {} < {} + {}'.format(m1, l1, l2, l3))
print('{} < {} < {} + {}'.format(m2, l2, l1, l3))
print('{} < {} < {} + {}'.format(m3, l3, l1, l2))
print('')
if (m1 < l1 < l2 + l3) and (m2 < l2 < l1 + l3) and (m3 < l3 < l1 + l2):
    print('As retas digitadas formam um triângulo:', end='') #o end= '' elimina o ender do proximo print
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1==l2 or l2==l3 or l3==l1:
        print('ISÓCELES')
    else:
        print('ESCALENO ')
else:
    print('As retas não formam um triângulo')