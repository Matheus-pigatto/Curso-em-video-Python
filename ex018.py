import math
ang = float(input('Digite um angulo: '))
angr = math.radians(ang)
cos = math.cos(angr)
seno = math.sin(angr)
tag = math.tan(angr)
print('O valor do cosseno para o angulo {}o é  {:.2f}'.format(ang, cos))
print('O valor do seno para o angulo {}o é {:.2f}'.format(ang, seno))
print('O valor da tangente do angulo {}o é {:.2f}'.format(ang, tag))
