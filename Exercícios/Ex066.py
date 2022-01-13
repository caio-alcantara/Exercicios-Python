num = sum = contador = 0
while True:
    num = int(input("Digite um valor: [999 para parar] "))
    if num == 999:
        break
    sum += num
    contador += 1
print(f"Foram digitados {contador} valores. A soma deles vale {sum}.")
