lista = []
for p in range(1, 6):
    peso = float(input(f"Digite o peso da {p}ª pessoa: "))
    lista.append(peso)
print(f"O maior peso entre essas pessoas é de {max(lista)}kg.")
print(f"O menor peso entre essas pessoas é de {min(lista)}kg.")
