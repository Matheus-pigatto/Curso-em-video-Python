def fatorial(n, show=False):
    """
    Help on function fatorial in module __main__:

    fatorial(n, show=False)
    -> Calcula o Fatorial de um número
    :param n: o número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial de um número n
    """
    resultado=n
    c = 1
    a = n-c
    print('-----'*n)
    print(f' {n} X', end='')
    if show==True:
        while c < n:
            resultado = a*resultado
            print(f' {a} ', end='')
            if n > c+1:
                print('X', end='')
            else:
                print('=', end=' ')
            c+=1
            a=a-1
    else:
        while c < n-1:
            resultado = (n-c)*resultado
            c += 1
        print(resultado)

    return resultado

print(fatorial(5,show=True))