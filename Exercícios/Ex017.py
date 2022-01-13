# Crie um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# e dê a medida de sua hipotenusa
from numpy import pow, sqrt
cop = int(input("Quanto mede o cateto oposto? "))
cad = int(input("Quanto mede o cateto adjacente? "))
hipotenusa = sqrt(pow(cop, 2) + pow(cad, 2))
print(f"A hipotenusa deste triângulo retângulo mede {hipotenusa} ")
