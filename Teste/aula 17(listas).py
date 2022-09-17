lanche =['pizza','suco','pudim', 'picolé']
print(lanche)
lanche[3]='cookie'
print(lanche)
lanche.insert(0,'Cachorro quente')
print(lanche)
del lanche[3]
print(lanche)
lanche.pop(3)
print(lanche)
lanche.remove('pizza')
print(lanche)
lanche.append('pizza')
print(lanche)
#lanche.pop() elimina o ultimo indice

valores = list(range(4,11))
print(valores)
valores.sort()#ordena os valores
valores.sort(reverse=True)# inverte a ordenação do da lista
print(valores)
print(len(valores))#o len é util para fazer laços