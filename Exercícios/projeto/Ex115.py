from lib.interface import *

arquivo = 'pessoas.txt'
if arquivoExiste('pessoas.txt'):
    print('Arquivo encontrado.')
else:
    criarArquivo('pessoas.txt')

choice = escolha()
while choice != 3:
    if choice == 1:
        head('Pessoas Cadastradas:'.upper())
        print(f"{'Nome:':<35}{'Idade:':>}")
        leiaArquivo('pessoas.txt')
        from time import sleep

        sleep(0.5)

        choice = escolha()

    if choice == 2:
        head("Cadastrar nova pessoa:".upper())
        age = 0
        name = str(input("Digite um nome: ")).strip().title()
        while name == '':
            name = str(input("Nome inválido. Digite um nome: ")).strip().title()
        while True:
            try:
                age = int(input("Digite a idade: "))
            except (ValueError, TypeError):
                print("A idade tem que ser um número inteiro.")
                continue
            else:
                break
        escreveArquivo(name, age)

        from time import sleep

        sleep(0.5)

        choice = escolha()

    if choice == 3:
        head("SAINDO DO SISTEMA.")
        from time import sleep

        sleep(0.5)
        from sys import exit

        exit()