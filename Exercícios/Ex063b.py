n = int(input("Digite um valor: "))
t1 = 0
t2 = t3 = 1
contador = 4
print(f"{t1} -> {t2} -> {t3}", end='')
while contador <= n:
    t4 = t2 + t3
    print(f" -> {t4}", end='')
    t2 = t3
    t3 = t4
    contador += 1
print(" -> Fim", end='')