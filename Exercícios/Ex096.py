# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.


def area(a, b):
    print(f"A área desse terreno {a}x{b} é de {a * b}m^2")


# Programa principal
largura = float(input("Digite a largura do terreno, em metros: "))
comprimento = float(input("Digite o comprimento desse terreno, em metros: "))
area(largura, comprimento)
