#Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os numa lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final,
# serão exibidos todos os valores únicos digitados, em ordem crescente.
continuar = ''
lista = []
while continuar != 'N':
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado!")
    else:
        print(f"O número {n} já foi digitado. Por isso, não o adicionarei novamente.")
    continuar = str(input("Quer digitar outro valor? [S/N] ")).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input("Você não digitou uma opção válida. Quer digitar outro valor? [S/N] ")).strip().upper()
print("=" * 60)
print(f"Os valores digitados, em ordem crescente, foram {sorted(lista)}")