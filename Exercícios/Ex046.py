# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
tempo = int(input("Quantos segundos você quer que a contagem dure? "))
print("\33[7mA contagem regressiva irá começar!\33[m")
sleep(2)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print("\33[7;31mKABOOOM!\33[m")