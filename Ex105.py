def notas(*num, sit=True):
    """
    -> Função para analizar notas, e situação de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação do aluno
    :return:dicionario com várias informações sobre a situação da turma
    """
    Dnotas = dict()
    Dnotas['total'] = len(num)
    Dnotas['maior'] = max(num)
    Dnotas['menor'] = min(num)
    Dnotas['média'] = sum(num)/len(num)
    if sit:
        if Dnotas['média'] >= 7:
            Dnotas['situação'] = 'Boa'
        elif Dnotas['média'] > 5 and Dnotas['média'] < 7:
            Dnotas['situação'] = 'Razoavel'
        else:
            Dnotas['situação'] = 'Ruim'
    return Dnotas

resp = notas(5.5, 2.5, 10, 6.5, sit=False)
print(resp)
help(notas)