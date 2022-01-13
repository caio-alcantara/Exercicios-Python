# Escreva um programa que leia dois números inteiros e compare-os, dizendo qual é o maior, ou se os dois têm mesmo valor
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
if n1 > n2:
    print(f"O valor {n1} é maior do que o valor {n2}.")
elif n2 > n1:
    print(f"O valor de {n2} é maior do que o valor de {n1}.")
else:
    print(f"Os valores {n1} e {n2} são iguais.")