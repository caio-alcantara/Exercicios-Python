# Faça um programa que leia o preço de um produto e mostre o preço desse mesmo produto com 5% de desconto.
p = float(input("Qual o preço do produto? "))
d = p - (p * (5/100))
print(f"O preço desse produto é de {p:.2f} reais. O preço com desconto de 5% é de {d:.2f} reais")
