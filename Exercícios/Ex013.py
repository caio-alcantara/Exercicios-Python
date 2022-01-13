# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
s = float(input("Qual é o seu salário atual? "))
ns = s + (s * (15/100))
print(f"O seu salário atual é de {s:.2f} reais. Com o aumento de 15%, o seu salário passará a ser de {ns} reais. ")
