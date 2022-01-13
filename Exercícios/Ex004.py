# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e algumas infoormações sobre ele.
n = input('Digite algo: ')
print(f"O tipo primitivo desse valor é: {type(n)}")
print(f"É alfabético? {n.isalpha()}")
print(f"Está em maíúsculas? {n.isupper()}")
print(f"Está em minusculas? {n.islower()}")
print(f"É numérico? {n.isnumeric()}")
print(f"Pode ser impresso? {n.isprintable()}")
print(f"É alfanumérico? {n.isalnum()}")
