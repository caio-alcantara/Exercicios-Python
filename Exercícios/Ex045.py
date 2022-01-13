from random import choice
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)
print("Vamos jogar jokenpô? Vou escolher pedra, papel ou tesoura e você faça o mesmo. Vamos ver quem ganha!")
player = str(input("Você escolheu pedra, papel, ou tesoura? ")).strip().capitalize()
print("Agora, eu vou escolher também!")
print("\33[7mESCOLHENDO...\33[m")
sleep(1)
if pc == player:
    print(f"Vejamos.... Eu escolhi {pc}. Ihh... Deu empate. ")
elif pc == 'Pedra' and player == 'Papel':
    print(f"Vejamos.... Eu escolhi {pc}. Ah, parece que você ganhou. :(")
elif pc == 'Papel' and player == 'Pedra':
    print(f"Vejamos.... Eu escolhi {pc}. Ha! Parece que eu ganhei.")
elif pc == 'Tesoura' and player == 'Pedra':
    print(f"Vejamos.... Eu escolhi {pc}. Ah, parece que você ganhou. :(")
elif pc == 'Pedra' and player == 'Tesoura':
    print(f"Vejamos.... Eu escolhi {pc}. Ha! Parece que eu ganhei.")
elif pc == 'Papel' and player == 'Tesoura':
    print(f"Vejamos.... Eu escolhi {pc}. Ah, parece que você ganhou. :(")
elif pc == 'Tesoura' and player == 'Papel':
    print(f"Vejamos.... Eu escolhi {pc}. Ha! Parece que eu ganhei.")
else:
    print("Opa! Parece que você não digitou um valor válido. ")
