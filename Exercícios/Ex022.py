# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas. -
# Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
nome = input("Digite um nome:")
a = nome.replace(" ", "")
abc = nome.split()
print(f"O nome {nome} escrito somente em letras minúsculas fica: {nome.lower()}")
print(f"O mesmo nome escrito somente em letras maíúsculas fica: {nome.upper()}")
print(f"A quantidade de caractéres nesse nome, sem considerar espaços, é de {len(a)} caractéres ")
print(f"O primeiro nome possui {len(abc[0])} caractéres. ")
