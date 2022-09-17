def Titulo(A):
    comprimento_do_texto = int(len(A)+6)
    print(f"{'~' * comprimento_do_texto}")
    print(A.center(comprimento_do_texto))
    print(f"{'~' * comprimento_do_texto}")


#Programa principal
texto =str(input())
Titulo(texto)