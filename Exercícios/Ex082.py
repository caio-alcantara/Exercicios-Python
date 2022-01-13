# Crie um programa que vai ler vários números e colocar numa lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista_total = []
lista_pares = []
lista_impares = []
continuar = ''
while continuar != 'N':
    num = int(input("Digite um valor: "))
    lista_total.append(num)
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
    continuar = str(input("Deseja digitar outro valor? [S/N] ")).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input("Opção inválida. Deseja digitar um novo valor? [S/N] ")).strip().upper()
print(f"A lista com todos os números é {lista_total}")
if len(lista_pares) >= 1:
    print(f"A lista com somente os números pares é {lista_pares}")
else:
    print("Não foram digitados valores pares.")
if len(lista_impares) >= 1:
    print(f"A lista com somente os números ímpares é {lista_impares}")
else:
    print("Não foram digitados valores ímpares")