# Elabore um programa que calcule o preço a ser pago por um produto
prec = float(input("Em reais, qual é o valor total do produto? "))
pag = str(input("Qual a condição de pagamento? Á vista, à vista no cartão, duas vezes no cartão ou três vezes no cartão? ")).strip().title()
if pag == 'À Vista':
    print(f"O preço a ser pago é de R${prec - (10/100 * prec):.2f}.")
elif pag == 'À Vista No Cartão':
    print(f"O preço a ser pago é de R${prec - (5/100 * prec):.2f}.")
elif pag == 'Duas Vezes No Cartão':
    print(f"O preço a ser pago é de R${prec:.2f}, dividido em duas parcelas de {prec / 2:.2f}.")
elif pag == 'Três Vezes No Cartão':
    print(f"O preço a ser pago é de R${prec + (20/100 * prec):.2f}, divido em três parcelas de R${(prec + (20/100 * prec)) / 3:.2f}.")
