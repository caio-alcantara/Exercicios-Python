# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from time import sleep
from random import randint
from operator import itemgetter

valores = {}
valores_sortidos = []
quantidade = int(input("Quantos jogadores irão participar? "))
print('-=' * 30)
print("Valores sorteados:")
print('-=' * 30)
for c in range(1, quantidade + 1):
    valores[f'Jogador {c}'] = randint(1, 6)
    print(f"Jogador {c} tirou {valores[f'Jogador {c}']} no dado.")
    sleep(0.5)
valores_sortidos = sorted(valores.items(), key=itemgetter(1), reverse=True)
sleep(0.5)
print(f"-=" * 30)
print("RANKING:")
print("-=" * 30)
sleep(0.5)
for i, v in enumerate(valores_sortidos):
    print(f"{i+1}º lugar: {v[0]}, com {v[1]} no dado.")
    sleep(0.5)
print('-=' * 30)
print(f"O ganhador foi o {valores_sortidos[0][0]}, que foi o primeiro a tirar {valores_sortidos[0][1]} no dado.")
