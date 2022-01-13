# Crie um programa que faça o computador "pensar" em um número inteiro de 0 a 5 e peça para o jogador
# tentar adivinhar qual foi o número escolhido pelo computador
from random import randint
from sys import exit
print("Vamos jogar um jogo! Eu vou pensar em um número de 0 a 5, e você vai tentar adivinhar.")
num = randint(0, 5)
print("Pronto! Eu já pensei em um número. Agora é a sua vez de adivinhar!")
g = int(input("Qual é o seu primeiro chute? "))
if g == num:
    print("Parabéns, você acertou de primeira! Alguns diriam que foi pura sorte...")
    exit()
else:
    continuar = str(input("HAHA! Você errou. Quer continuar jogando até acertar? Responda com 'Sim' ou 'Não'")).strip().capitalize()
if continuar == 'Sim':
    print("Então vamos continuar jogando!")
else:
    print("Então paramos por aqui, com você sendo um perdedor. HAHAHAHAHAHA!")
    exit()
g1 = int(input("Qual o seu segundo chute? "))
if g1 == num:
    print("Parabéns! Você acertou")
    exit()
else:
    print("Você errou! Continue tentando!")
g2 = int(input("Qual o seu terceiro chute? "))
if g2 == num:
    print("Parabéns! Você acertou.")
    exit()
else:
    print("Errrrooooouuuuu!")
g3 = int(input("Qual seu quarto chute? "))
if g3 == num:
    print("Parabéns, você acertou!")
    exit()
else:
    print("Até quando você vai continuar errando?")
g4 = int(input("Qual o seu quinto chute? "))
if g4 == num:
    print("Parabéns, você acertou!")
    exit()
else:
    print(f"Você conseguiu a façanha de errar todos os chutes... a repostas correta é: {num}")
