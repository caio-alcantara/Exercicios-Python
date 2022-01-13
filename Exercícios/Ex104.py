# Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante à função input() do Python,
# porém, fazendo a validação para aceitar apenas um valor numérico. Ex.: n = leiaInt(‘Digite um n: ‘)


def leia_int(text):
    while True:
        try:
            num = int(input(text))
        except (ValueError, TypeError):
            print(f"\33[33;7mOpção Inválida! Este não é um número inteiro.\33[m")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário.")
            return '<nulo>'
        else:
            return num


def leia_float(text):
    while True:
        try:
            num = float(input(text))
        except (ValueError, TypeError):
            print("\33[33;7mOpção Inválida! Este não é um número racional.\33[m")
            continue
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário.")
            return '<nulo>'
        else:
            return num


# Programa principal
inteiro = leia_int("Digite um número inteiro: ")
racional = leia_float("Digite um número racional: ")
print(f"Você digitou o valor inteiro {inteiro}, e o valor racional {racional}.")