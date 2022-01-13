from time import sleep
num_1 = int(input("Digite um valor: "))
num_2 = int(input("Digite outro valor: "))
option = 0
lista = [num_1, num_2]
while option != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    option = int(input("Qual opção você deseja realizar? "))
    if option == 1:
        print(f"A soma desses valores vale: {num_1 + num_2}.")
    elif option == 2:
        print(f"A multiplicação desses valores vale: {num_1 * num_2}.")
    elif option == 3:
        print(f"O maior valor dentre esses dois é {max(lista)}.")
    elif option == 4:
        print("Informe os números novamente:")
        num_1 = int(input("Digite um valor: "))
        num_2 = int(input("Digite outro valor: "))
        lista = [num_1, num_2]
    elif option == 5:
        print("\33[7mTERMINANDO O PROGRAMA...\33[m")
        sleep(0.75)
    else:
        print("Opção inválida.")
    sleep(1)
print("\33[7mFIM DO PROGRAMA. VOLTE SEMPRE!\33[m")
