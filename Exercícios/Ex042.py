# Refaça o exercício 35 (triângulos), mas agora mostrando se o triangulo é equilátero, isósceles ou escaleno.
from sys import exit
r1 = int(input("Qual o valor da primeira reta? "))
r2 = int(input("Qual o valor da segunda reta? "))
r3 = int(input("Qual o valor da terceira reta? "))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r3 + r2) > r1:
    print(f"Usando as medidas {r1}, {r2} e {r3}, pode-se construir um triângulo!")
else:
    print(f"Usando as medidas {r1}, {r2} e {r3}, não se pode construir um triângulo.")
    exit()
if r1 == r2 == r3:
    print("Este triângulo é \33[7mequilátero.\33[m")
elif r1 == r2 or r1 == r3 or r2 == r3:
    print("Este triângulo é \33[7misósceles.\33[m")
elif r1 != r2 and r1 != r3 and r2 != r3:
    print("Este triângulo é \33[7mescaleno.\33[m")
