# Faça um programa que leia o valor de um ângulo qualquer e mostre na tela o valor de sen, cos e tan desse ângulo
from numpy import radians, sin, cos, tan
ang = float(input("Qual o valor do ângulo? "))
cos = cos(radians(ang))
sen = sin(radians(ang))
tan = tan(radians(ang))
print(f"O cosseno desse ângulo é {cos:.2f}\n o seno desse ângulo é {sen:.2f}\n e a tangente desse ângulo é {tan:.2f} ")


