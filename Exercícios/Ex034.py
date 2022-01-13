# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input("Qual o salário atual? "))
if sal > 1250:
    print(f"Após o aumento, o salário de R${sal:.2f} passará a ser de R${(10/100 * sal) + sal:.2f}")
else:
    print(f"Após o aumento, o salário de R${sal:.2f} passará a ser de R${(15/100 * sal) + sal:.2f}")
    