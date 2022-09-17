def aumentar(num = 0, por = 0):
    aumentar = num * (1 + (por/100))
    return aumentar


def diminuir(num = 0, por = 0):
    diminuir = num * (1 - (por/100))
    return diminuir


def dobro(num = 0):
    dobro = num * 2
    return dobro


def metade(num = 0):
    metade = num / 2
    return metade


def moeda(num = 0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')

