# Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(anos):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - anos
    if idade < 16:
        return f'Essa pessoa tem {idade} anos e, portanto, tem o voto NEGADO.'
    if 16 <= idade < 18 or idade >= 65:
        return f'Essa pessoa tem {idade} anos e, portanto, tem o voto OPCIONAL.'
    if idade >= 18:
        return f'Essa pessoa tem {idade} anos e, portanto, tem o voto OBRIGATÓRIO.'
    return idade


# Programa principal
nascimento = int(input("Digite o ano de nascimento: "))
print(voto(nascimento))
