# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
nums = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f"Foram sorteados os valores {nums}")
print(f"O menor valor é {sorted(nums)[0]}")
print(f"O maior valor é {sorted(nums)[-1]}")