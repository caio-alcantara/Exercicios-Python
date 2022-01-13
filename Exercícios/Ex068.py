from random import randint
vitorias = 0
print("Vamos jogar par ou ímpar.")
while True:
    opcao = str(input("Você escolhe par ou ímpar? [P/I] ")).strip().capitalize()[0]
    num = int(input("Digite um valor de 0 a 10: "))
    pc = randint(1, 10)
    soma = pc + num
    if opcao == 'P' and soma % 2 == 0:
        print(f"Parabéns, você ganhou. Eu escolhi o número {pc}. {pc} + {num} = {soma}")
        vitorias += 1
    elif opcao == 'P' and soma % 2 != 0:
        print(f"Você perdeu. Eu escolhi o número {pc}. {pc} + {num} = {soma}")
        break
    elif opcao == 'I' and soma % 2 != 0:
        print(f"Parabéns, você ganhou. Eu escolhi o número {pc}. {pc} + {num} = {soma}")
        vitorias += 1
    elif opcao == 'I' and soma % 2 == 0:
        print(f"Você perdeu. Eu escolhi o número {pc}. {pc} + {num} = {soma}")
        break
print(f"Você conseguiu {vitorias} vitórias consecutivas.")