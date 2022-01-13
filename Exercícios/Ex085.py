# Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
valores = [[], []]
for c in range(1, 8):
    num = int(input(f"Digite o {c}o valor: "))
    valores.append(num)
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
if len(valores[0]) > 0:
    print(f"Os valores pares digitados foram {sorted(valores[0])}")
else:
    print("Não foram digitados valores pares.")
if len(valores[1]) > 0:
    print(f"Os valores ímpares digitados foram {sorted(valores[1])}")
else:
    print("Não foram digitados valores ímpares.")