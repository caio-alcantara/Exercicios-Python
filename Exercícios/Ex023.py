# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input("Digite um número inteiro de 0 - 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Analisando o número {num}, temos que: ")
print(f"Unidade: {u*1}")
print(f"Dezena: {d*10}")
print(f"Centena: {c*100}")
print(f"Milhar é: {m*1000}")
