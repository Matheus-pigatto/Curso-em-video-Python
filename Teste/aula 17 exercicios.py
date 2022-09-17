num = [2,5,9,1]
num[2]=3
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
for c, v in enumerate(num): #o enumerate utiliza a posicão em c e o valor em v#
    print(f'Na posição {c} encontrei o valor {v}... ')#, end='')
print(max(num))
print(min(num))