#  Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input("Qual o seu nome? ")).strip().title()
print(f"Existe um 'Silva' no seu nome? {'Silva' in nome}")