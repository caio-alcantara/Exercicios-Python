n = soma = quantidade = 0
while n != 999:
    n = int(input("Digite um valor: [999 para parar] "))
    quantidade += 1
    soma += n
    if n == 999:
        soma -= 999
        quantidade -= 1
print(f"Foram digitados {quantidade} números. A soma deles é {soma}.")
