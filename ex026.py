f = str(input('Digite uma frase: ')).upper()
f =f.strip()
print(f)
cnt = f.count("A")
l1 = f.find("A")
l2 =f.rfind("A")
print('A frase escrita tem {} A '.format(cnt))
print('A posição da primeira letra A é {}'.format(l1+1))
print('A posição da ultima letra A é {}'.format(l2+1))

