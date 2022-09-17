def aviso(menssagem):
    print('-'*40)
    print(f" {str(menssagem):^40}")
    print('-' *40)
aviso('sistema de alunos')


def soma(a, b):
    print(f' A = {a} e B = {b}')
    s = a + b
    print(f' A soma A + B = {s}')


#programa principal
aviso(soma(4, 5))
print()
soma(10, 8)
soma(b=1, a=5)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    return(print(lst))

valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)