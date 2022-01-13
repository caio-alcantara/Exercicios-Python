# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
for c in range(0, 5):
    lista.append(int(input(f"Digite um valor para a posição {c}: ")))
print(lista)
print(f"O maior valor na lista é {max(lista)}, nas posições", end=' ')
for index, valor in enumerate(lista):
    if valor == max(lista):
        print(f"{index}...", end=' ')
print(f"\nO menor valor na lista é {min(lista)}, nas posições", end=' ')
for index, valor in enumerate(lista):
    if valor == min(lista):
        print(f"{index}...", end=' ')
