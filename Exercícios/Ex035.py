# Desenvolva um programa que leia o comprimento de três retas,
# e diga ao usuário se elas podem ou não formar um triângulo.
r1 = int(input("Qual o valor da primeira reta? "))
r2 = int(input("Qual o valor da segunda reta? "))
r3 = int(input("Qual o valor da terceira reta? "))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r3 + r2) > r1:
    print(f"Usando as medidas {r1}, {r2} e {r3}, pode-se construir um triângulo!")
else:
    print(f"Usando as medidas {r1}, {r2} e {r3}, não se pode construir um triângulo.")
