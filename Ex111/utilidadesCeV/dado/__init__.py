def leiaDinheiro(preço):
    validador = isinstance(preço)
    if validador is False:
        print(f'"{preço}" é um preço invalido')
