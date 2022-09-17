def ajuda(msg):
    import time
    while True:
        cabeçario = 'SISTEMA DE AJUDA PyHELP'
        print('\033[1;42m''~'*int(len(cabeçario)+4))
        print(cabeçario)
        print('~' * int(len(cabeçario) + 4))
        print('\033[m',end='')
        pesquisa = str(input(msg)).lower().lstrip()
        if pesquisa == 'fim':
            print('\033[1;31m''~' * int(len('fim') + 4))
            print('fim'.center(len('fim')+4))
            print('~' * int(len('fim') + 4))
            print('\033[m', end='')
            break
        time.sleep(0.5)
        psq = 'Acessando o manual do comando'
        print('\033[1;46m''~' * int(len(psq) + 10))
        print(f'{psq} "{pesquisa}"'.center(len(psq) + 10))
        print('~' * int(len(psq) + 10))
        print('\033[m', end='')
        time.sleep(0.5)
        print('\033[47;30m')
        help(pesquisa)
        print('\033[0m')


ajuda('Função ou Biblioteca >')