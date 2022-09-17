def aumentar(num=0, por=0, format=False):
    aumentar = num * (1 + (por / 100))
    return aumentar if format is False else (moeda(aumentar))


def diminuir(num=0, por=0, format=False):
    diminuir = num * (1 - (por / 100))
    return diminuir if format is False else (moeda(diminuir))


def dobro(num=0, format=False):
    dobro = num * 2
    return dobro if format is False else (moeda(dobro))


def metade(num=0, format=False):
    metade = num / 2
    return metade if format is False else(moeda(metade))


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')


def resumo(num=0, aumento=0, diminui=0, format=False):
    print(f'-'*40)
    print(f'RESUMO DO VALOR'.center(40))
    print(f'-'*40)
    print(f'Preço analisado:          \t{moeda(num)}')
    print(f'Dobro do preço:           \t{dobro(num,format)}')
    print(f'Metade do preço:          \t{metade(num,format)}')
    print(f'{aumento}% de auemnto:          \t{aumentar(num,aumento,format)}')
    print(f'{diminui}% de redução:           \t{diminuir(num,diminui,format)}')

    print(f'-' * 40)
