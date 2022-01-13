# Escreva um programa que leia um número e, de acordo com escolha, o converta para outras bases numéricas
num = int(input("Digite um número inteiro: "))
base = int(input("Para qual base você quer converter este número? Use 1 para binário, 2 para octal e 3 para hexadecimal: "))
if base == 1:
    print(f"O número {num} em base binária é {bin(num)}.")
elif base == 2:
    print(f"O número {num} em base octal é {oct(num)}.")
elif base == 3:
    print(f"O número {num} em base hexadecimal é {hex(num)}.")
else:
    print(f"Você não escolheu uma opção válida.")