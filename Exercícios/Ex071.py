valor = int(input("Digite o valor que deseja sacar: "))
cedulas_1 = 0
cedulas_10 = 0
cedulas_50 = valor // 50
cedulas_20 = (valor % 50) // 20
resto = (valor % 50) % 20
if resto < 10:
    cedulas_1 += resto
else:
    cedulas_10 += resto // 10
    cedulas_1 += resto % 10
print("Você receberá este valor em:")
print(f"{cedulas_50} cédulas de R$50,00")
print(f"{cedulas_20} cédulas de R%20,00")
print(f"{cedulas_10} cédulas de R$10,00")
print(f"{cedulas_1} moedas de R$1,00")
