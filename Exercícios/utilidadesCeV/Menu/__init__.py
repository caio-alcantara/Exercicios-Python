def menu():
    print('-=' * 15)
    print(f'{"MENU PRINCIPAL":^30}')
    print('-=' * 15)
    for c in range(1, 4):
        if c == 1:
            print(f'{c} -', 'Ver pessoas cadastradas')
        elif c == 2:
            print(f'{c} -', 'Cadastrar nova pessoa')
        elif c == 3:
            print(f'{c} -', 'Sair do sistema')
    print('-=' * 15)


def opcao(text):
    choice = 0
    while choice != 3:
        while True:
            try:
                choice = int(input(text))
                if choice > 3 or choice == 0:
                    print(f"Não existe opção {choice}. Digite outro valor.")
                    continue
            except (ValueError, TypeError):
                print("Valor digitado é inválido. Digite outro valor: ")
                continue
            break
        if choice == 1:
            print('-=' * 15)
            print(f'{"OPÇÃO 1":^30}')
            print('-=' * 15)

            menu()
            opcao("Opção: ")

        if choice == 2:
            print('-=' * 15)
            print(f'{"OPÇÃO 2":^30}')
            print('-=' * 15)

            menu()
            opcao("Opção: ")

        if choice == 3:
            print('-=' * 15)
            print(f'{"SAINDO DO SISTEMA":^30}')
            print('-=' * 15)
            from sys import exit
            exit()

        break