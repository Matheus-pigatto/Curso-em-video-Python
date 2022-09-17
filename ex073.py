Camp_braz = ('Atletico - MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'Americana- MG',
             'Atletico - GO', 'Santos', 'Ceará - SC', 'Internacional', 'São Paulo', 'Athletico - PR', 'Cuiabá', 'Juventude', 'Grêmio',
             'Bahia', 'Sport Recife', 'Chapecoense')
lista = list(Camp_braz)
pos = Camp_braz.index('Chapecoense')
print(f'Os 5 primeiro times do brazileirao são {Camp_braz[0:5]}')
print('='*120)
print(f'Os 5 último da tabela do brasileirõ são {Camp_braz[15:20]}')
print('='*120)
print(f'Times em ordem alfabética: {sorted(Camp_braz)}')
print('='*120)
print(f'A Chapecoense está na posição {Camp_braz.index("Chapecoense")+1}ª do Brasileirão')