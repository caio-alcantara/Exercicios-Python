# Escreva um programa que verifique se uma pessoa pode fazer um empréstimo, baseando-se no valor da casa, do salario,
# e das prestações, sendo que o empréstimo será negado caso o valor das prestações seja maior do que 30% do salário.
casa = float(input("Qual o valor da casa desejada? "))
sal = float(input("Qual o salário do comprador? "))
anos = int(input("Em quantos anos o comprador pretende pagar essa casa? "))
prest = casa / (anos * 12)
if prest > (30/100 * sal):
    print("Infelizmente, o seu empréstimo foi negado. Lamentamos o ocorrido. ")
else:
    print(f"Parabéns, você conseguiu o empréstimo! O valor das prestações mensais fica em R${prest:.2f}, sendo pago durante {anos * 12} meses.")