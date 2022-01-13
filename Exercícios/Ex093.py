# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []

jogador['Nome'] = str(input("Nome do jogador: "))
partidas = int(input("Quantas partidas foram jogadas por esse jogador? "))

for c in range(1, partidas + 1):
    gols.append(int(input(f"Quantos gols foram marcados na {c}ª partida? ")))
    jogador['Gols marcados em cada partida'] = gols[:]
    jogador['Total de gols'] = sum(jogador['Gols marcados em cada partida'])

print('-=' * 30)
print(jogador)
print('-=' * 30)

for key, value in jogador.items():
    print(f"{key}: {value}")
print('-=' * 30)

print(f"O jogador {jogador['Nome']} jogou {partidas} partidas.")
for c in range(0, partidas):
    print(f"   => Na partida {c + 1}, marcou {gols[c]} gol(s).")
print(f"Foi um total de {jogador['Total de gols']} gols.")