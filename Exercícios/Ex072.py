# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
           'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    while num > 20 or num < 0:
        num = int(input("Você não digitou uma opção válida. Digite um número entre 0 e 20: "))
    print(f"Você digitou o número '{extenso[num]}'.")
    continuar = str(input("Você quer digitar outro número? [S/N] ")).strip().capitalize()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input("Você não digitou uma opção válida. Quer continuar? [S/N] "))
    if continuar == 'N':
        break