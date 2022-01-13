lista = []
continuar = ''
while continuar != 'N':
    lista.append(int(input("Digite um valor: ")))
    continuar = str(input("Quer digitar outro valor? [S/N} ")).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input("Você não digitou uma opção válida. Deseja digitar outro valor? [S/N] ")).strip().upper()
print(f"Foram digitados {len(lista)} valores.")
lista.sort(reverse=True)
print(f"A lista de valores, ordenada de forma decrescente, fica: {lista}.")
if 5 in lista:
    print(f"O número 5 aparece nesta lista {lista.count(5)} vez(es).")
else:
    print("O número 5 não foi digitado.")