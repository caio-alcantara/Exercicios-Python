# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
#
# — Quantidade de valores digitados
# — A maior nota
# — A menor nota
# — A média da turma
# — A situação (opcional)


def notas(*valores, sit=False):
    """
    -> Função que analisa uma quantidade n de notas de alunos, e retorna um dicionário com os valores:
       Quantidade de notas adicionadas; maior nota; menor nota; média das notas;
    :param valores: As notas adicionadas, e que irão ser analizadas.
    :param sit: Parâmetro opcional que, se verdadeiro, mostra a situação da turma.
           Situação = 'BOA' caso a média das notas seja maior ou igual a 7.
                      'RUIM' caso seja menor que 5.
                      'RAZOÁVEL' caso esteja entre 5 e 7.
    :return: dicionário com informações extraídas a partir das notas.
    """
    dic = {'Total de notas': len(valores), 'Maior nota': max(valores), 'Menor nota': min(valores),
           f'Média das {len(valores)} notas': f"{sum(valores)/len(valores):.2f}"}
    if sum(valores) / len(valores) < 5:
        situacao = 'RUIM'
    elif 5 <= sum(valores) / len(valores) < 7:
        situacao = 'RAZOÁVEL'
    else:
        situacao = 'BOA'
    if sit is True:
        dic['Situação'] = situacao
        return dic

    else:
        return dic


print(notas(10, 9, 8, 4, 5, 6, 10, 1, 5, 7, 1, 9, 8.5, 9.3, sit=True))
help(notas)
