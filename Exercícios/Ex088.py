# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint
lista = []
jogos = []
quantidade = int(input("Quantos jogos você quer sortear? "))
tot = 0
while tot < quantidade:
    contador = 0
    while contador != 6:
        num = randint(1, 60)
        if num not in lista:
            jogos.append(num)
            contador += 1
    jogos.sort()
    lista.append(jogos[:])
    jogos.clear()
    tot += 1
print(f"Sorteando {quantidade} jogos.")
for i, l in enumerate(lista):
    print(f"Jogo {i+1}: {l}")