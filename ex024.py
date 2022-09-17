# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com santo
nome = str(input('Digite o nome da cidade: '))
nome = nome.strip()
nome = nome.capitalize()
lista = nome.split()
print('A cidade {} começa com santo? {}'.format(nome,nome[:5] == "Santo"))