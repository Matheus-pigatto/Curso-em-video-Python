def voto(ano):
    import datetime
    ano_atual = datetime.date.today().year
    idade = ano_atual-ano
    if idade < 18 and idade > 15 or idade > 70:
        voto_ = 'Voto Opcional'
    elif idade >18 and idade <= 70:
        voto_ ='Voto Obrigatório'
    else:
        voto_ = 'Não Vota'
    return idade, voto_


ano = int(input('Em que ano você nasceu? '))
voto_ = voto(ano)
print(f'Com {voto_[0]} anos:{voto_[1]}.')