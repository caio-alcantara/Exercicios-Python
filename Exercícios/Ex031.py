# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# C50alcule o preço da passagem, cobrando R$0, por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
km = float(input("Qual a distância da sua viagem em quilômetros? "))
if km <= 200:
    print(f"O preço da sua passagem será de R${0.5 * km:.2f}")
else:
    print(f"O preço da sua viagem será de R${0.45 * km:.2f}")
