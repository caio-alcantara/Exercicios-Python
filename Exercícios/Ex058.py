from random import randint
print("Vamos jogar um jogo! Eu vou pensar em um número de 0 a 10, e você vai tentar adivinhar.")
num = randint(0, 10)
print("Pronto! Eu já pensei em um número. Agora é a sua vez de adivinhar!")
attempts = 0
guess = 0
while guess != num:
    guess = int(input("Tente adivinhar o número no qual eu pensei: "))
    if guess > 10:
        print("Opa, lembre que eu falei que ia pensar num número de 0 a 10? Tente novamente.")
    elif guess > num:
        print("Chute mais baixo.")
        attempts += 1
    elif guess < num:
        print("Chute mais alto.")
        attempts += 1
    elif guess == num:
        attempts += 1
        print(f"Parabéns! Você acertou, e só precisou de {attempts} tentativas, HAHAHAHA! Eu pensei no número {num}.")
