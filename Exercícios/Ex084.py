# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

continuar = ''
pesado = leve = 0
dados = []
pessoas = []

while continuar != 'N':
    dados.append(str(input("Digite o nome da pessoa: ")).strip())
    dados.append(float(input("Digite o peso dessa pessoa: ")))

    if len(pessoas) == 0:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados[1] < leve:
            leve = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    continuar = str(input("Deseja adicionar outra pessoa? [S/N] ")).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input("Você não digitou um valor válido. Quer continuar? [S/N] ")).strip().upper()

print(f"Ao todo, foram cadastradas {len(pessoas)} pessoas")
print(f"O maior peso foi de {pesado}Kg. Sendo o peso de:", end=' ')
for p in pessoas:
    if p[1] == pesado:
        print(f'[{p[0]}]', end='')
print()
print(f"O menor peso foi de {leve}Kg. Sendo o peso de:", end=' ')
for p in pessoas:
    if p[1] == leve:
        print(f"[{p[0]}]", end='')
print()