# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = terceira_coluna = maior_segunda = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite o valor da posição [{linha}, {coluna}]: "))

        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end='')
    print()

print(f"A soma dos valores pares dessa matriz é {pares}.")
print(f"A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}.")
print(f"O maior número na segunda linha é {max(matriz[1])}.")
