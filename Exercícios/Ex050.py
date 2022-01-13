import numpy
soma = 0
count = 0
for c in range(1, 7):
    num = int(input(f"Digite o {c}º valor: "))
    if num % 2 == 0:
        soma += num
        count += 1
print(f"Foram informados {count} valores pares. A soma deles é {soma}.")