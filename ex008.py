#escreva um programa que leia um valor digirado em metros e o converta para centimetro ou milimetros

print('='*50)
F1='conversora de metro'
print('              Conversora de Metro          ')
n = float(input('Digite um comprimento em metros:'))
km = n*0.0001
hm = n*0.001
dam = n*0.1
dm = n*10
cm = n*100
mm = n*1000
print('{} metros correspondem a:'.format(n))
print('{} Kilometros:'.format(km))
print('{} Hectometro:'.format(hm))
print('{} Decâmetro:'.format(dam))
print('{:.3f} Decimetro:'.format(dm))
print('{:.0f} Centimetro:'.format(cm))
print('{:.0f} Milimetros:'.format(mm))


