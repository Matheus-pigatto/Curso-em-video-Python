from ex115.sistema.menu import menu, opcao, itens
import ex115.sistema.cores as c
import time

def menuDisp():
    while True:
        menu('MENU INICIAL')
        itens(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])

        # validação da opção escolhida
        while True:
            try:
                op = int(input(f'{c.cor(9)}Sua Opção:{c.cor(0)} '))
            except(ValueError, TypeError):
                print(c.cor(8), 'ERRO! Digite uma opção valida!', c.cor(0))
                continue
            else:
                if op > 3 or op < 0:
                    print(c.cor(8), 'ERRO! Digite um numero valido!', c.cor(0))
                    time.sleep(0.5)
                    menu('MENU INICIAL')
                    itens(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
                    continue
                else:
                    break
        if op == 3:
            menu('Saindo do sistema... Até logo!')
            break
        else:
            opcao(op)
        return op

def verCadastro():
    arq = open('cursoemvideo.txt', 'r')
    print(arq.read())


def cadastrarPessoa():
    arq = open('cursoemvideo.txt', 'a')
    while 1:
        nome = str(input('Digite um nome: '))
        if not nome.isnumeric() != True:
            print('Digite soemnte Letras!')
            continue
        else:
            break
    while 1:
        try:
            idade = int(input('Digte a idade da pessoa: '))
        except(ValueError, TypeError):
            print(c.cor(8), 'ERRO! Digite um numero valido!', c.cor(0))
            continue
        else:
            break
    pessoacadastrada = (f'{nome:<35} {idade} anos')
    arq.write('\n')
    arq.write(pessoacadastrada)
    arq.close
    print(f'{nome} cadastrada com sucesso!')
