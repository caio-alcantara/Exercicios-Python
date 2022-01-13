# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
tup1 = ()
pares = ()
for c in range(1, 6):
    n = int(input("Valor: "))
    tup1 += (n,)
    if n % 2 == 0:
        pares += (n,)
print(f"Os valores digitados foram: {tup1}.")
print(f"O número 9 foi digitado {tup1.count(9)} vezes.")
if 3 in tup1:
    print(f"O número 3 apareceu pela primeira vez na posição {tup1.index(3) + 1}.")
else:
    print("O número 3 não foi digitado nenhuma vez.")
print(f"Os valores pares digitados foram {pares}.")