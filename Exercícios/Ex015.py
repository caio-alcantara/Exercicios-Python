# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado,
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input("Quantos quilômetros foram rodados? "))
dias = int(input("Por quantos dias o carro foi alugado? "))
pago = (dias * 60) + (km * 0.15)
print(f"O preço a ser pago por este aluguel é de R${pago:.2f}. ")
