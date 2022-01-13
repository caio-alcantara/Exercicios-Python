# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = input("Qual o nome da cidade? ")
a = cidade.strip().capitalize()
print(f"A cidade {a} possui 'Santo' no nome? {'Santo' in a[:5]}")



