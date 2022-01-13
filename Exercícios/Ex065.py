numero = soma = contador = maior = menor = 0
continuar = ''
lista_maior_menor = []
while continuar != 'N':
    numero = int(input("Digite um valor: "))
    lista_maior_menor.append(numero)
    contador += 1
    soma += numero
    continuar = str(input("Deseja digitar outro número? [SIM/NÃO] ")).strip().capitalize()[0]
    while continuar != 'S' and continuar != 'N':
        print("Você não digitou um valor válido.")
        continuar = str(input("Deseja digitar outro número? [SIM/NÃO] ")).strip().capitalize()[0]
print(f"Foram digitados {contador} números. A média deles é {soma/contador}. ")
print(f"O maior valor digitado foi {max(lista_maior_menor)}, e o menor foi {min(lista_maior_menor)}.")