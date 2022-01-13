# Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá conseguir mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome='desconhecido', gols=0):
    return f'O jogador {nome} marcou {gols} gol(s)'


# Programa principal

jogador = str(input("Nome do jogador: "))
if len(jogador) == 0:
    jogador = '<desconhecido>'

gols_marcados = str(input(f"Quantos gols foram marcados por {jogador}? "))
if gols_marcados.isnumeric() is True:
    gols_marcados = int(gols_marcados)
else:
    gols_marcados = 0

print(ficha(jogador, gols_marcados))
