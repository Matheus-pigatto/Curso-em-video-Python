lag = float(input('Qual a largura da parede: '))
alt = float(input('qual a altura da parede: '))
area = lag*alt
tinta = (area)/2
print('Para pintar uma parede com {}m² você ira precisar de {:.2f}l de tinta'.format(area, tinta))
