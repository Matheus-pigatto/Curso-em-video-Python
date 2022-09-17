import interface
import os

pesqArq = os.listdir()
if 'cursoemvideo.txt' not in pesqArq:
    arq = open('cursoemvideo.txt', 'w')
    print('O arquivo cursoemvideo.txt foi criado com sucesso ')
while True:
    respMenu = interface.menuDisp()
    if respMenu == 1:
        interface.verCadastro()
    elif respMenu == 2:
        interface.cadastrarPessoa()
    else:
        break
